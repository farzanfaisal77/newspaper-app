start with creating venv, installing django then start project
startapp accounts
add it in installed apps and auth user model
design db CustomUser in models (from AbstractUser) with age field (for now)
AbstractUser lets us define everything instead of just the default fields
making custom user creation and change forms (Meta fields are default fields)
making custom admin and registering on site (fieldsets and addfieldsets for extra fields on edit and creating for the extra fields)
forms and templates for homepage login logout etc
update urls and views
pages app for homepageview
bootstrap:pip install:  django-crispy-forms, crispy-bootstrap5
password change forms (most stuff are builtin)
password forgetting - using sendgrid in production

using mixins to make sure only loged in ppl access cetrain urls
LoginRequiredMixin, UserPassesTestMixin