from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
import pdb
# Create your models here.
class Jobs(models.Model):
    """Model for jobs registering. It includes a job identifier, two files R1 and R2 and a email
    field for sending the results.
    """
    job_id = models.CharField(_("Job identifier"),max_length=20,null=True)
    file_R1 = models.FileField(upload_to="data",null=True)
    file_R2 = models.FileField(upload_to="data",null=True)
    email = models.EmailField(_("Email"),null=True)

    def __str__(self):
        return self.file_R1.name

    @models.permalink
    def get_absolute_url(self):
        return ('upload-new', )

    def save(self, *args, **kwargs):
        #pdb.set_trace()
        #self.job_id = "1"
        super(Jobs, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        """delete -- Remove to leave file."""
        self.file_R1.delete(False)
        super(Jobs, self).delete(*args, **kwargs)
