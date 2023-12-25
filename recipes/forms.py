from django import forms


class PostForm(forms.Form):
    title = forms.CharField(label='Название', max_length=100,
                            widget=forms.TextInput(attrs={'class': 'form-control',
                                                          'placeholder': 'Введите название'}))
    description = forms.CharField(label='Описание',
                                  widget=forms.Textarea(
                                      attrs={'class': 'form-control', 'placeholder': 'Введите описание'}))
    steps_cooking = forms.CharField(label='Процесс приготовления',
                                    widget=forms.Textarea(
                                        attrs={'class': 'form-control', 'placeholder': 'Распишите рецепт по шагам'}))
    time_for_cooking = forms.IntegerField(label='Время готовки',
                                          widget=forms.NumberInput(attrs={'class': 'form-control'}))
    photo = forms.ImageField(label='Фото')
