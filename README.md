# 🏢 Korean VC Proposal Automation Platform
## 2025 KIF (한국정보통신진흥기금) GP 선정 자동화 시스템

### 📋 Overview
정부 모태펀드 RFP 제안서 작성을 자동화하는 웹 기반 플랫폼입니다. 운용사의 재사용 가능한 데이터를 관리하고, RFP 요구사항을 분석하여 Excel 제안서를 자동 생성합니다.

### 🚀 Quick Start

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Run the application
streamlit run app.py

# 3. Open browser (automatically opens)
# Default URL: http://localhost:8501
```

### 📁 Project Structure

```
VCRFP-1/
├── app.py                 # Main application
├── requirements.txt       # Python dependencies
├── README.md             # Documentation
├── vc_proposal_platform.db  # SQLite database (auto-created)
└── sample_data/          # Example files (optional)
    ├── sample_rfp.pdf
    └── sample_template.xlsx
```

### 🎯 Key Features

#### 1. **User Authentication**
- Secure login system with password hashing
- Multi-tenant support for different VC firms
- Session management

#### 2. **Data Vault Dashboard**
- Visual status indicators for 21 standard sheets
- Categorized view (재무정보, 인력정보, 운용실적, etc.)
- Reusability indicators (High/Medium/Low)

#### 3. **Smart Data Input**
- Sheet-specific forms with validation
- Korean format support (날짜: YYYY.MM.DD, 금액: 백만원)
- Version control for different RFPs

#### 4. **RFP Analysis**
- PDF parsing for requirements extraction
- Automatic detection of:
  - Mandatory investment percentages (의무투자)
  - Submission deadlines (제출기한)
  - Target sectors (AI, 5G, 바이오, etc.)
  - Fund size (펀드 규모)

#### 5. **Automated Generation**
- Excel template auto-filling
- Formula preservation
- Data validation
- Downloadable output

### 📊 Sheet Categories

| Category | Sheets | Reusability |
|----------|--------|------------|
| **기본정보** | 표지 | Low |
| **펀드구성** | 1-0, 1-1 제안펀드 구성 | Low |
| **재무정보** | 1-2 재무실적, 1-3 납입자본금 | High |
| **인력정보** | 1-4 핵심운용인력, 3-1~3-4 인력 상세 | High |
| **운용실적** | 2-1~2-3 펀드 실적 | High |
| **투자전략** | 2-4~2-5 전략 및 계획 | Medium |
| **수수료** | 4-1~4-2 보수체계 | Medium |
| **컴플라이언스** | 5-1~5-2 이해상충/제재 | High |

### 🔧 Core Functions

```python
# Parse RFP requirements
rfp_info = parse_rfp_pdf("rfp_document.pdf")
# Returns: {'mandatory_investment': '60% AI/ICT', 'deadline': '2025-08-28', ...}

# Load Excel template structure
template = parse_excel_template("submission_template.xlsx")
# Returns: {'sheet_name': {'fields': {...}, 'formulas': {...}}, ...}

# Compare and analyze
comparison = compare_data(stored_data, rfp_info, template)
# Returns: {'available': [...], 'missing': [...], 'suggestions': [...]}

# Generate filled Excel
output_path = generate_filled_excel(template_path, stored_data)
```

### 💾 Database Schema

```sql
-- Users table
users (
    id INTEGER PRIMARY KEY,
    username VARCHAR(100) UNIQUE,
    password_hash VARCHAR(256),
    firm_name VARCHAR(200),
    created_at DATETIME
)

-- Proposal data table  
proposal_data (
    id INTEGER PRIMARY KEY,
    user_id INTEGER FOREIGN KEY,
    sheet_id VARCHAR(50),
    data_json TEXT,  -- JSON stored data
    version VARCHAR(100),  -- 'base', '2025 KIF Version', etc.
    created_at DATETIME,
    updated_at DATETIME
)
```

### 🎨 UI Workflow

1. **Login/Register**
   - Create account with firm name
   - Secure authentication

2. **Upload Documents**
   - RFP PDF (공고문)
   - Excel Template (제출 양식)

3. **Review Data Vault**
   - Check completion status
   - Identify missing data

4. **Input/Update Data**
   - Fill sheet-specific forms
   - Validate and save

5. **Analyze Requirements**
   - View RFP requirements
   - Get improvement suggestions

6. **Generate Proposal**
   - Select data version
   - Download filled Excel

### 📝 Input Validation Rules

- **Dates**: YYYY.MM.DD format (e.g., 2025.08.28)
- **Amounts**: Numeric only, 백만원 unit
- **Percentages**: 0-100 range
- **No zeros**: Use blank for empty financial fields
- **Required fields**: CEO/대표이사 information mandatory

### 🔒 Security Features

- SHA-256 password hashing
- Session-based authentication
- SQL injection prevention via ORM
- Input sanitization
- Secure file handling

### 🐛 Troubleshooting

| Issue | Solution |
|-------|----------|
| **Port already in use** | `streamlit run app.py --server.port 8502` |
| **Database locked** | Close other instances or delete `vc_proposal_platform.db` |
| **PDF parsing fails** | Ensure PDF is text-based, not scanned image |
| **Excel formula errors** | Check template compatibility (xlsx format required) |
| **Korean text display** | Ensure UTF-8 encoding support |

### 📈 Performance Tips

1. **Batch Operations**: Upload all documents before processing
2. **Data Reuse**: Mark high-reusability sheets as 'base' version
3. **Version Control**: Create "2025 KIF Version" for specific modifications
4. **Regular Saves**: Platform auto-saves on each form submission

### 🔄 Version Management

- **Base Version**: Core reusable data
- **2025 KIF Version**: RFP-specific modifications
- **Custom Versions**: User-defined variations
- Version inheritance: Later versions override base data

### 📊 Sample Data Format

```json
{
  "1-2.재무실적": {
    "유동자산_2023년": 5000,
    "비유동자산_2023년": 3000,
    "자산총계_2023년": 8000,
    "매출액_2023년": 12000,
    "영업이익_2023년": 2000,
    "당기순이익_2023년": 1500
  },
  "1-4.핵심운용인력": {
    "성명_0": "김대표",
    "직위_0": "대표이사",
    "경력년수_0": 15,
    "성명_1": "이전무",
    "직위_1": "전무이사",
    "경력년수_1": 12
  }
}
```

### 🚦 Platform Status Indicators

- ✅ **Green**: Data complete (>80% filled)
- ⚠️ **Yellow**: Partial data (30-80% filled)
- ❌ **Red**: Missing data (<30% filled)

### 📱 Browser Compatibility

- Chrome 90+ (Recommended)
- Firefox 88+
- Safari 14+
- Edge 90+

### 🆘 Support

For issues or questions:
1. Check the troubleshooting section
2. Review error messages in the UI
3. Check browser console for detailed errors
4. Restart the application if needed

### 📄 License

This platform is designed specifically for Korean VC firms participating in government fund-of-funds programs.

### 🎯 Roadmap

- [ ] Multi-language support (Korean/English)
- [ ] Cloud deployment options
- [ ] Advanced analytics dashboard
- [ ] API integration with government portals
- [ ] Automated compliance checking
- [ ] Team collaboration features

---

**Made for Korean VCs** | **2025 KIF Ready** | **정부 모태펀드 최적화**