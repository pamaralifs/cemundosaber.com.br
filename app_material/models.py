from django.db import models
from django.contrib.auth.models import User
from app_nivel_escolar.models import NivelEscolar
from app_serie_escolar.models import SerieEscolar

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    #return 'materiais/%Y/%m/%d/user_{0}/{1}'.format(instance.usuario.id, filename)
    return 'materiais/{0}_{3}_{4}_{5}_user_{1}/{2}'.format(instance.id,instance.usuario.id,filename,instance.data_hora_upload.strftime('%Y'),instance.data_hora_upload.strftime('%m'),instance.data_hora_upload.strftime('%d'))


class Material(models.Model):
    VISIVEL_CHOICES = [ ('S','Sim'), ('N','Não') ]
    titulo = models.CharField(max_length=255,unique=True,verbose_name='Título')
    arquivo = models.FileField(upload_to=user_directory_path,verbose_name='Arquivo')
    visivel = models.CharField(choices=VISIVEL_CHOICES,max_length=1,verbose_name='Visível',default='S')
    data_hora_upload = models.DateTimeField(auto_now_add=True,verbose_name='Publicado em')
    data_hora_alteracao = models.DateTimeField(auto_now=True,verbose_name='Alterado em')
    nivel_escolar = models.ForeignKey(NivelEscolar,on_delete=models.PROTECT,related_name='materiais',verbose_name='Nível',null=True)
    serie_escolar = models.ForeignKey(SerieEscolar,on_delete=models.PROTECT,related_name='materiais',verbose_name='Série',null=True)
    usuario = models.ForeignKey(User,on_delete=models.PROTECT,related_name='materiais',verbose_name='Usuário',null=True)

    def __str__(self):
        return self.titulo

    # https://stackoverflow.com/questions/9968532/django-admin-file-upload-with-current-model-id
    def save(self, *args, **kwargs):
        if self.pk is None:
            saved_arquivo = self.arquivo
            self.arquivo = None
            super(Material, self).save(*args, **kwargs)
            self.arquivo = saved_arquivo
            if 'force_insert' in kwargs:
                kwargs.pop('force_insert')
        super(Material, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Material'
        verbose_name_plural = "Materiais"
        