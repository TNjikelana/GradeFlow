#!/bin/bash

# Root folder
# mkdir -p GradeFlow
# cd GradeFlow

# Core app structure
mkdir -p app/auth app/models app/templates/auth app/templates/dashboard app/static/css app/static/js app/static/img app/utils

# Files inside app
touch app/__init__.py
touch app/auth/routes.py app/auth/forms.py app/auth/services.py
touch app/models/user.py app/models/mark.py
touch app/templates/base.html app/templates/auth/login.html app/templates/auth/register.html app/templates/dashboard/index.html
touch app/static/css/main.css app/static/js/main.js
touch app/utils/validation.py app/utils/name_generator.py
touch app/config.py app/extensions.py app/dashboard.py  # renamed from routes.py

# Root-level files
mkdir -p tests migrations
touch tests/test_auth.py tests/test_models.py
touch .env .gitignore config.py run.py requirements.txt

echo "✅ GradeFlow project structure created with recommended layout."
