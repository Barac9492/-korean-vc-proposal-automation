"""
Streamlit app optimized for Vercel deployment
Korean VC Proposal Automation Platform - Demo Version
"""

import streamlit as st
import pandas as pd
import json
from datetime import datetime
import os

# Configure Streamlit page
st.set_page_config(
    page_title="Korean VC Proposal Automation | 2025 KIF GP Selection",
    page_icon="🏢",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better UI
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(90deg, #1f77b4 0%, #17a2b8 100%);
        padding: 1rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
    }
    .feature-card {
        background: #f8f9fa;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 4px solid #1f77b4;
        margin-bottom: 1rem;
    }
    .metric-card {
        background: white;
        padding: 1rem;
        border-radius: 8px;
        border: 1px solid #dee2e6;
        text-align: center;
    }
    .highlight-box {
        background: #e3f2fd;
        padding: 1rem;
        border-radius: 8px;
        border-left: 4px solid #2196f3;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

def main():
    """Main application"""
    
    # Header
    st.markdown("""
    <div class="main-header">
        <h1>🏢 Korean VC Proposal Automation Platform</h1>
        <h3>2025 KIF GP Selection Optimized System</h3>
        <p>✅ Live Demo | Real Template Support | Production Ready</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Quick stats
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
        <div class="metric-card">
            <h2>1,200+</h2>
            <p>Lines of Code</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="metric-card">
            <h2>19</h2>
            <p>KIF Sheet Templates</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="metric-card">
            <h2>60%</h2>
            <p>Mandatory Investment</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
        <div class="metric-card">
            <h2>Aug 28</h2>
            <p>2025 Deadline</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Main tabs
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "🎯 Overview", 
        "📊 2025 KIF Requirements", 
        "💼 Platform Demo",
        "🚀 Installation",
        "📚 Documentation"
    ])
    
    with tab1:
        show_overview()
    
    with tab2:
        show_kif_requirements()
    
    with tab3:
        show_platform_demo()
    
    with tab4:
        show_installation()
    
    with tab5:
        show_documentation()

def show_overview():
    """Display platform overview"""
    st.header("🎯 Platform Overview")
    
    st.markdown("""
    <div class="highlight-box">
        <h4>🎉 Complete Automation Solution for Korean VC Firms</h4>
        <p>This platform automates the entire process of preparing government fund proposals, 
        specifically optimized for the <strong>2025 KIF (Korean Information and Communications Fund) GP Selection</strong>.</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### 🎯 Key Benefits
        - **⏰ Time Savings**: 2-3 weeks → 2-3 days
        - **📊 100% Compliance**: Real KIF template support
        - **🔄 Reusability**: Data persists across RFPs
        - **🛡️ Enterprise Security**: SHA-256 encryption
        - **🇰🇷 Korean Optimized**: Native language support
        """)
        
        st.markdown("""
        ### 🏆 Success Metrics
        - Complete 2025 KIF integration
        - 19 real sheet templates
        - Automatic PDF parsing
        - Excel generation with formulas
        - Enterprise-ready deployment
        """)
    
    with col2:
        st.markdown("""
        ### 🔧 Technical Features
        - **Smart PDF Analysis**: Extract RFP requirements automatically
        - **Template Parsing**: Detect Excel field types and structure
        - **Data Validation**: KIF-specific format checking
        - **Version Control**: Track changes across submissions
        - **Gap Analysis**: Identify missing requirements
        """)
        
        st.markdown("""
        ### 📈 Platform Architecture
        - **Frontend**: Streamlit (Python web framework)
        - **Backend**: SQLite with SQLAlchemy ORM
        - **File Processing**: openpyxl, PyPDF2, pdfplumber
        - **Security**: Session-based authentication
        - **Deployment**: Vercel serverless platform
        """)

def show_kif_requirements():
    """Display 2025 KIF requirements"""
    st.header("📊 2025 KIF GP Selection Requirements")
    
    # Key details
    st.subheader("🎯 핵심 정보")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.error("**⏰ 접수마감**\n2025년 8월 28일(목) 16:00")
        st.info("**💰 총 출자규모**\n1,500억원")
    
    with col2:
        st.info("**📊 조합 수**\n16개")
        st.warning("**🎯 의무투자**\n60% 이상")
    
    with col3:
        st.info("**⏳ 존속기간**\n8년 이내")
        st.info("**🏢 GP 출자**\n약정총액의 1% 이상")
    
    # Investment areas
    st.subheader("🎯 투자 분야")
    
    areas_data = {
        "분야": ["AI·AX 혁신", "AI·ICT (운용사 제안)", "ICT 기술사업화", "AI 반도체"],
        "조합 수": ["3개", "10개", "1개", "2개"],
        "KIF 출자액": ["450억원", "750억원", "100억원", "200억원"],
        "최소 결성액": ["900억원", "1,500억원", "200억원", "400억원"]
    }
    
    df_areas = pd.DataFrame(areas_data)
    st.dataframe(df_areas, use_container_width=True)
    
    # Personnel requirements
    st.subheader("👥 핵심운용인력 요구사항")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **최소 인원 구성**
        - 총 3인 이상 참여 (대표펀드매니저 1인 포함)
        - 200억원 이하 펀드: 2인 이상
        
        **경력 요건**
        - 대표펀드매니저: 5년 이상
        - 기타 핵심인력: 3년 이상
        """)
    
    with col2:
        st.markdown("""
        **선정 절차**
        1. 1차 심의 (서류평가)
        2. 현장실사
        3. 2차 심의 (PT발표평가)
        4. 최종선정 (우선협상대상자)
        
        **최종 결과**: 2025년 9월 중 발표
        """)
    
    # Exclusion criteria
    st.subheader("❌ 선정 배제 대상")
    
    exclusions = [
        "기존 KIF 펀드 투자비율 60% 미만",
        "최근 KIF 펀드 선정 후 2년 미경과",
        "자본잠식률 50% 이상",
        "대표펀드매니저 제재 이력 (3년 이내)",
        "법령 위반 또는 시정명령 미이행 상태"
    ]
    
    for exclusion in exclusions:
        st.error(f"• {exclusion}")

def show_platform_demo():
    """Display platform demo"""
    st.header("💼 Platform Demo")
    
    demo_tab1, demo_tab2, demo_tab3, demo_tab4 = st.tabs([
        "📊 Data Vault", 
        "✏️ Input Forms", 
        "🔍 Analysis", 
        "📄 Generation"
    ])
    
    with demo_tab1:
        st.subheader("📊 Data Vault Dashboard")
        
        # Completion metrics
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("✅ Completed", "12", "sheets")
        with col2:
            st.metric("⚠️ Partial", "5", "sheets")
        with col3:
            st.metric("❌ Missing", "2", "sheets")
        
        # Category progress
        st.subheader("Category Progress")
        
        categories = {
            "재무정보": 0.85,
            "인력정보": 0.70,
            "운용실적": 0.95,
            "투자전략": 0.45,
            "컴플라이언스": 0.60
        }
        
        for category, progress in categories.items():
            st.progress(progress, f"{category} ({progress*100:.0f}%)")
    
    with demo_tab2:
        st.subheader("✏️ Sample Input Form")
        st.markdown("#### 1-2. 재무실적 (Demo)")
        
        with st.form("demo_financial"):
            col1, col2 = st.columns(2)
            
            with col1:
                st.number_input("유동자산 (백만원)", value=5000, help="2023년 기준")
                st.number_input("비유동자산 (백만원)", value=3000)
                st.number_input("매출액 (백만원)", value=12000)
            
            with col2:
                st.number_input("자본총계 (백만원)", value=8000)
                st.number_input("영업이익 (백만원)", value=2000)
                st.number_input("당기순이익 (백만원)", value=1500)
            
            if st.form_submit_button("💾 저장 (Demo)", use_container_width=True):
                st.success("✅ Demo data saved successfully!")
                st.balloons()
    
    with demo_tab3:
        st.subheader("🔍 RFP Analysis Sample")
        
        # Sample RFP info
        st.markdown("#### 📋 Detected RFP Requirements")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.error("**⏰ 접수마감**: 2025-08-28 (D-15)")
            st.info("**💰 총 출자규모**: 1,500억원")
            st.warning("**🎯 의무투자**: 60% 이상")
        
        with col2:
            st.info("**📊 조합 수**: 16개")
            st.info("**⏳ 존속기간**: 8년 이내")
            st.info("**🏢 GP 출자**: 약정총액의 1% 이상")
        
        # Improvement suggestions
        st.markdown("#### 💡 개선 제안")
        suggestions = [
            "AI/인공지능 투자 전략을 '2-4.투자전략 및 계획'에 추가 필요",
            "AI 분야 투자 실적을 '2-3.KIF 펀드 운용실적'에 강조",
            "핵심운용인력 경력 요건 재검토 (5년/3년 이상)"
        ]
        
        for suggestion in suggestions:
            st.warning(f"• {suggestion}")
    
    with demo_tab4:
        st.subheader("📄 Excel Generation Demo")
        
        st.markdown("#### 🎯 Generation Process")
        
        process_steps = [
            "✅ Load stored data from database",
            "✅ Apply 2025 KIF template structure", 
            "✅ Fill cells with validation",
            "✅ Preserve formulas and formatting",
            "✅ Generate downloadable Excel file"
        ]
        
        for step in process_steps:
            st.info(step)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.metric("Template Sheets", "19")
            st.metric("Fields Detected", "150+")
        
        with col2:
            st.metric("Completion Rate", "85%")
            st.metric("Validation Errors", "0")
        
        if st.button("🚀 Generate Demo Excel", use_container_width=True):
            st.success("✅ Excel proposal generated successfully!")
            st.info("📥 In the full version, this would download: `KIF_제안서_운용사명_20250813.xlsx`")

def show_installation():
    """Show installation instructions"""
    st.header("🚀 Installation & Setup")
    
    install_tab1, install_tab2, install_tab3 = st.tabs([
        "💻 Local Setup",
        "🌐 GitHub Repository", 
        "☁️ Cloud Deployment"
    ])
    
    with install_tab1:
        st.subheader("💻 Local Installation")
        
        st.markdown("#### Prerequisites")
        st.code("""
# Required
- Python 3.11+
- Git
- Modern web browser (Chrome, Firefox, Safari)
        """)
        
        st.markdown("#### Quick Setup")
        st.code("""
# Clone repository
git clone https://github.com/[USERNAME]/korean-vc-proposal-automation.git
cd korean-vc-proposal-automation

# Install dependencies
pip install -r requirements.txt

# Run application
streamlit run app.py

# Access at http://localhost:8501
        """, language="bash")
        
        st.markdown("#### Alternative Setup")
        st.code("""
# Auto-installation script
chmod +x setup.sh
./setup.sh
        """, language="bash")
    
    with install_tab2:
        st.subheader("🌐 GitHub Repository")
        
        st.markdown("""
        #### Repository Structure
        ```
        korean-vc-proposal-automation/
        ├── 🎯 app.py                    # Full application
        ├── 🌐 streamlit_app.py          # This demo
        ├── 📦 requirements.txt          # Dependencies
        ├── 📖 README.md                 # Documentation
        ├── 🛠 DEPLOYMENT.md             # Technical guide
        ├── 📋 KIF_2025_GUIDE.md         # KIF guide
        └── 📁 .streamlit/               # Configuration
        ```
        """)
        
        st.markdown("#### Key Features")
        features = [
            "✅ Complete 2025 KIF integration",
            "✅ 19 real sheet templates",
            "✅ Automatic PDF parsing",
            "✅ Excel generation with formulas",
            "✅ Enterprise security",
            "✅ Comprehensive documentation"
        ]
        
        for feature in features:
            st.info(feature)
    
    with install_tab3:
        st.subheader("☁️ Cloud Deployment")
        
        st.markdown("#### Vercel Deployment")
        st.code("""
# 1. Push to GitHub
git push origin main

# 2. Deploy to Vercel
- Go to vercel.com
- Import GitHub repository
- Auto-deploy with vercel.json

# 3. Access live demo
https://korean-vc-proposal-automation.vercel.app
        """)
        
        st.markdown("#### Alternative Platforms")
        
        platforms = {
            "Streamlit Cloud": "Free hosting for Streamlit apps",
            "Heroku": "Container-based deployment",
            "Railway": "Simple Git-based deployment", 
            "DigitalOcean": "App Platform deployment"
        }
        
        for platform, description in platforms.items():
            st.info(f"**{platform}**: {description}")

def show_documentation():
    """Show documentation links"""
    st.header("📚 Documentation")
    
    doc_tab1, doc_tab2, doc_tab3 = st.tabs([
        "📖 User Guides",
        "🛠 Technical Docs", 
        "🎯 KIF Specific"
    ])
    
    with doc_tab1:
        st.subheader("📖 User Guides")
        
        guides = [
            {
                "title": "README.md",
                "description": "Complete project overview and quick start guide",
                "topics": ["Installation", "Features", "Usage", "Support"]
            },
            {
                "title": "KIF_2025_GUIDE.md", 
                "description": "Specific guide for 2025 KIF GP selection process",
                "topics": ["Requirements", "Templates", "Validation", "Tips"]
            },
            {
                "title": "RELEASE_NOTES.md",
                "description": "Complete feature overview and platform capabilities", 
                "topics": ["Features", "Updates", "Technical specs", "Roadmap"]
            }
        ]
        
        for guide in guides:
            with st.expander(f"📄 {guide['title']}"):
                st.write(guide['description'])
                st.write("**Topics covered:**")
                for topic in guide['topics']:
                    st.write(f"• {topic}")
    
    with doc_tab2:
        st.subheader("🛠 Technical Documentation")
        
        tech_docs = [
            {
                "title": "DEPLOYMENT.md",
                "description": "Technical deployment and configuration guide",
                "audience": "Developers, System Administrators"
            },
            {
                "title": "GITHUB_DEPLOYMENT_GUIDE.md",
                "description": "Step-by-step GitHub and Vercel deployment",
                "audience": "DevOps, Project Managers"
            },
            {
                "title": "API Documentation",
                "description": "Function references and code structure",
                "audience": "Developers, Contributors"
            }
        ]
        
        for doc in tech_docs:
            with st.expander(f"🔧 {doc['title']}"):
                st.write(doc['description'])
                st.write(f"**Target audience**: {doc['audience']}")
    
    with doc_tab3:
        st.subheader("🎯 KIF-Specific Documentation")
        
        st.markdown("""
        #### 2025 KIF GP Selection Resources
        
        **Official Requirements**
        - Sheet template structure (19 sheets)
        - Field validation rules
        - Date format requirements (YYYY-MM-DD)
        - Personnel qualification criteria
        
        **Platform Optimization**
        - Korean text parsing
        - KIF-specific validation
        - Template field mapping
        - Requirement compliance checking
        
        **Success Factors**
        - Data completeness strategies
        - Common error prevention
        - Submission best practices
        - Timeline management
        """)
        
        st.markdown("#### Quick Reference")
        
        quick_ref = {
            "접수마감": "2025년 8월 28일(목) 16:00",
            "총 출자규모": "1,500억원 (16개 조합)",
            "의무투자": "60% 이상",
            "핵심인력": "3인 이상 (5년/3년 경력)",
            "존속기간": "8년 이내"
        }
        
        for key, value in quick_ref.items():
            st.info(f"**{key}**: {value}")

# Footer
def show_footer():
    """Display footer"""
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center; padding: 2rem;'>
        <h3>🏆 Ready for 2025 KIF GP Selection</h3>
        <p><strong>Korean VC Proposal Automation Platform</strong></p>
        <p>Production Ready | Enterprise Security | KIF Optimized</p>
        <p><em>Perfect timing for the 2025 KIF GP selection process</em></p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
    show_footer()