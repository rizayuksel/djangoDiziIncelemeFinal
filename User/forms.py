from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label="Kullanıcı Adı")
    password = forms.CharField(label="Şifre", widget=forms.PasswordInput)

class RegisterForm(forms.Form):
    first_name = forms.CharField(max_length=30, label="Ad")
    last_name = forms.CharField(max_length=50, label="Soyad")
    email = forms.CharField(max_length=100, label="E-Mail")
    username = forms.CharField(max_length=30, label="Kullanıcı Adı")
    password = forms.CharField(max_length=20, label="Şifre", widget=forms.PasswordInput)
    confirm = forms.CharField(max_length=20, label="Şifre Tekrar", widget=forms.PasswordInput)
    
    def clean(self):
        first_name = self.cleaned_data.get("first_name")
        last_name = self.cleaned_data.get("last_name")
        email = self.cleaned_data.get("email")
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        confirm = self.cleaned_data.get("confirm")

        if(password and confirm and password != confirm):
            raise forms.ValidationError("Şifreler Eşleşmiyor...")
        
        values = {
            "first_name" : first_name,
            "last_name" : last_name,
            "email" : email,
            "username" : username,
            "password" : password
        }
        return values