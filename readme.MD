# Build : pyinstaller --onefile --add-data "assets:assets" fileName.py

# Linux build: pyinstaller --noconfirm --onefile --windowed --add-data "assets/\*:assets" app.py

# to binding the styles in the build file : pyinstaller --noconfirm --onefile --windowed --add-data "styles/_:styles" --add-data "assets/_:assets" main.py

# Windows Build: pyinstaller --noconfirm --onefile --windowed --add-data "assets/\*;assets" app.py
