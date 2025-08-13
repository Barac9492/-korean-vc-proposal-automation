#!/bin/bash

echo "🚀 Setting up Korean VC Proposal Automation Platform..."

# Check if pip is available
if ! command -v pip3 &> /dev/null; then
    echo "❌ pip3 not found. Please install Python and pip first."
    exit 1
fi

# Install requirements
echo "📦 Installing Python dependencies..."
pip3 install -r requirements.txt

# Verify installation
echo "✅ Verifying installation..."
python3 -c "
try:
    import streamlit
    import pandas
    import openpyxl
    import PyPDF2
    import sqlalchemy
    print('✅ All dependencies installed successfully!')
    print('🎯 Ready to run the platform')
    print('')
    print('To start the application:')
    print('  streamlit run app.py')
    print('')
    print('Platform will be available at: http://localhost:8501')
except ImportError as e:
    print(f'❌ Import error: {e}')
    print('Please check your Python environment and try again.')
"

echo ""
echo "🏢 Korean VC Proposal Platform Setup Complete!"
echo "   Run: streamlit run app.py"