#!/usr/bin/env bash
# exit on error
set -o errexit

echo "🔧 Instalando dependencias..."
pip install -r requirements.txt

echo "📦 Ejecutando migraciones..."
python manage.py migrate --noinput

echo "📁 Recolectando archivos estáticos..."
python manage.py collectstatic --no-input --clear

echo "✅ Build completado exitosamente!"
