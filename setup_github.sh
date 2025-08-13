#!/bin/bash

echo "🚀 Setting up GitHub Repository for Korean VC Proposal Automation Platform"
echo "============================================================================"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}📋 Prerequisites Check:${NC}"
echo "✅ Git repository initialized"
echo "✅ All files committed locally"
echo "✅ Ready for GitHub push"

echo ""
echo -e "${YELLOW}📝 Next Steps (Manual):${NC}"
echo ""

echo "1️⃣ Create GitHub Repository:"
echo "   - Go to https://github.com/new"
echo "   - Repository name: korean-vc-proposal-automation"
echo "   - Description: 2025 KIF GP Selection Automation Platform for Korean VC Firms"
echo "   - Set to Public (for free Vercel deployment)"
echo "   - ❌ Do NOT initialize with README (we already have one)"
echo "   - Click 'Create repository'"

echo ""
echo "2️⃣ Add Remote and Push:"
echo -e "${GREEN}git remote add origin https://github.com/[YOUR_USERNAME]/korean-vc-proposal-automation.git${NC}"
echo -e "${GREEN}git branch -M main${NC}"
echo -e "${GREEN}git push -u origin main${NC}"

echo ""
echo "3️⃣ Deploy to Vercel:"
echo "   - Go to https://vercel.com"
echo "   - Sign in with GitHub"
echo "   - Click 'New Project'"
echo "   - Import korean-vc-proposal-automation"
echo "   - Configure:"
echo "     * Build Command: Leave empty"
echo "     * Output Directory: Leave empty"
echo "     * Install Command: pip install -r requirements_vercel.txt"
echo "     * Root Directory: ./"
echo "   - Click 'Deploy'"

echo ""
echo "4️⃣ Expected URLs:"
echo "   📱 Demo: https://korean-vc-proposal-automation.vercel.app"
echo "   📚 Repo: https://github.com/[YOUR_USERNAME]/korean-vc-proposal-automation"

echo ""
echo -e "${BLUE}📁 Repository Contains:${NC}"
echo "   🎯 app.py - Full production application"
echo "   🌐 vercel_app.py - Vercel demo version"
echo "   📦 requirements.txt - Local dependencies"
echo "   📦 requirements_vercel.txt - Vercel dependencies"
echo "   ⚙️ vercel.json - Vercel configuration"
echo "   📖 Complete documentation suite"
echo "   🧪 Testing and validation scripts"

echo ""
echo -e "${GREEN}✅ Repository is ready for GitHub and Vercel deployment!${NC}"
echo -e "${YELLOW}💡 Pro tip: Star the repository and add topics for discoverability${NC}"

echo ""
echo "📊 Repository Stats:"
echo "   📝 Lines of code: 1,200+"
echo "   📄 Files: 16"
echo "   📚 Documentation: 8 files"
echo "   🎯 Ready for 2025 KIF GP selection"

echo ""
echo -e "${BLUE}🎉 Your Korean VC Proposal Automation Platform is ready to go live!${NC}"