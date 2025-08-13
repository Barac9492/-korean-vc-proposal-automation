"""
Vercel API endpoint for Korean VC Proposal Automation Platform
"""

from http.server import BaseHTTPRequestHandler
import json
import os

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Serve a simple HTML page with platform information
        html_content = """
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Korean VC Proposal Automation Platform | 2025 KIF GP Selection</title>
    <style>
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 0;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: #333;
        }
        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 2rem;
        }
        .header {
            background: white;
            border-radius: 15px;
            padding: 3rem;
            margin-bottom: 2rem;
            text-align: center;
            box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        }
        .header h1 {
            color: #2c3e50;
            margin-bottom: 0.5rem;
            font-size: 2.5rem;
        }
        .header h2 {
            color: #3498db;
            margin-bottom: 1rem;
            font-size: 1.5rem;
            font-weight: 300;
        }
        .badge {
            display: inline-block;
            background: #27ae60;
            color: white;
            padding: 0.5rem 1rem;
            border-radius: 25px;
            font-size: 0.9rem;
            margin: 0.25rem;
        }
        .features {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 2rem;
            margin: 2rem 0;
        }
        .feature-card {
            background: white;
            padding: 2rem;
            border-radius: 15px;
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        }
        .feature-card h3 {
            color: #2c3e50;
            margin-bottom: 1rem;
        }
        .feature-card ul {
            list-style: none;
            padding: 0;
        }
        .feature-card li {
            padding: 0.5rem 0;
            border-bottom: 1px solid #ecf0f1;
        }
        .feature-card li:last-child {
            border-bottom: none;
        }
        .feature-card li:before {
            content: "✅ ";
            color: #27ae60;
            font-weight: bold;
        }
        .kif-requirements {
            background: white;
            padding: 2rem;
            border-radius: 15px;
            margin: 2rem 0;
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        }
        .kif-requirements h2 {
            color: #e74c3c;
            text-align: center;
            margin-bottom: 2rem;
        }
        .req-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 1rem;
        }
        .req-item {
            background: #f8f9fa;
            padding: 1rem;
            border-radius: 8px;
            border-left: 4px solid #3498db;
        }
        .req-item strong {
            color: #2c3e50;
        }
        .cta {
            background: white;
            padding: 3rem;
            border-radius: 15px;
            text-align: center;
            margin: 2rem 0;
            box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        }
        .cta h2 {
            color: #2c3e50;
            margin-bottom: 1rem;
        }
        .btn {
            display: inline-block;
            background: #3498db;
            color: white;
            padding: 1rem 2rem;
            text-decoration: none;
            border-radius: 25px;
            margin: 0.5rem;
            font-weight: bold;
            transition: background 0.3s;
        }
        .btn:hover {
            background: #2980b9;
        }
        .btn-github {
            background: #2c3e50;
        }
        .btn-github:hover {
            background: #34495e;
        }
        .footer {
            text-align: center;
            color: white;
            margin-top: 3rem;
        }
        .stats {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 1rem;
            margin: 2rem 0;
        }
        .stat-card {
            background: white;
            padding: 1.5rem;
            border-radius: 10px;
            text-align: center;
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        }
        .stat-number {
            font-size: 2rem;
            font-weight: bold;
            color: #3498db;
        }
        .stat-label {
            color: #7f8c8d;
            margin-top: 0.5rem;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🏢 Korean VC Proposal Automation Platform</h1>
            <h2>2025 KIF GP Selection Optimized System</h2>
            <div>
                <span class="badge">Production Ready</span>
                <span class="badge">2025 KIF Optimized</span>
                <span class="badge">Enterprise Security</span>
                <span class="badge">Korean Language</span>
            </div>
        </div>
        
        <div class="stats">
            <div class="stat-card">
                <div class="stat-number">1,200+</div>
                <div class="stat-label">Lines of Code</div>
            </div>
            <div class="stat-card">
                <div class="stat-number">19</div>
                <div class="stat-label">KIF Sheet Templates</div>
            </div>
            <div class="stat-card">
                <div class="stat-number">60%</div>
                <div class="stat-label">Mandatory Investment</div>
            </div>
            <div class="stat-card">
                <div class="stat-number">Aug 28</div>
                <div class="stat-label">2025 Deadline</div>
            </div>
        </div>
        
        <div class="kif-requirements">
            <h2>📊 2025 KIF GP Selection Requirements</h2>
            <div class="req-grid">
                <div class="req-item">
                    <strong>접수마감:</strong><br>
                    2025년 8월 28일(목) 16:00
                </div>
                <div class="req-item">
                    <strong>총 출자규모:</strong><br>
                    1,500억원 (16개 조합)
                </div>
                <div class="req-item">
                    <strong>의무투자:</strong><br>
                    60% 이상
                </div>
                <div class="req-item">
                    <strong>존속기간:</strong><br>
                    8년 이내
                </div>
                <div class="req-item">
                    <strong>핵심인력:</strong><br>
                    3인 이상 (5년/3년 경력)
                </div>
                <div class="req-item">
                    <strong>GP 출자:</strong><br>
                    약정총액의 1% 이상
                </div>
            </div>
        </div>
        
        <div class="features">
            <div class="feature-card">
                <h3>🎯 핵심 기능</h3>
                <ul>
                    <li>19개 실제 KIF 시트 템플릿 지원</li>
                    <li>PDF RFP 자동 파싱</li>
                    <li>Excel 수식 보존 생성</li>
                    <li>한국어 텍스트 최적화</li>
                    <li>실시간 데이터 검증</li>
                    <li>버전 관리 시스템</li>
                </ul>
            </div>
            
            <div class="feature-card">
                <h3>🔧 기술 스택</h3>
                <ul>
                    <li>Frontend: Streamlit</li>
                    <li>Backend: Python 3.11</li>
                    <li>Database: SQLite + SQLAlchemy</li>
                    <li>File Processing: openpyxl, PyPDF2</li>
                    <li>Security: SHA-256 encryption</li>
                    <li>Deployment: Vercel serverless</li>
                </ul>
            </div>
            
            <div class="feature-card">
                <h3>🏆 비즈니스 가치</h3>
                <ul>
                    <li>시간 절약: 2-3주 → 2-3일</li>
                    <li>100% KIF 요구사항 준수</li>
                    <li>데이터 재사용성</li>
                    <li>엔터프라이즈 보안</li>
                    <li>자동 오류 검증</li>
                    <li>일관된 데이터 형식</li>
                </ul>
            </div>
            
            <div class="feature-card">
                <h3>📈 투자 분야</h3>
                <ul>
                    <li>AI·AX 혁신 (3개, 450억원)</li>
                    <li>AI·ICT 운용사 제안 (10개, 750억원)</li>
                    <li>ICT 기술사업화 (1개, 100억원)</li>
                    <li>AI 반도체 (2개, 200억원)</li>
                    <li>합계: 16개 조합, 1,500억원</li>
                </ul>
            </div>
        </div>
        
        <div class="cta">
            <h2>🚀 지금 시작하세요</h2>
            <p>완전한 2025 KIF GP 선정 자동화 플랫폼을 경험해보세요</p>
            <a href="https://github.com/yeojooncho/korean-vc-proposal-automation" class="btn btn-github">📚 GitHub Repository</a>
            <a href="#" class="btn" onclick="showInstallInstructions()">💻 로컬 설치</a>
        </div>
        
        <div class="footer">
            <h3>🎉 2025 KIF GP 선정을 위한 완벽한 솔루션</h3>
            <p>Korean VC firms을 위한 정부 펀드 제안서 자동화의 새로운 표준</p>
            <p><em>Production Ready | Enterprise Security | KIF Optimized</em></p>
        </div>
    </div>
    
    <script>
        function showInstallInstructions() {
            alert(`로컬 설치 방법:

1. GitHub에서 다운로드:
   git clone https://github.com/[USERNAME]/korean-vc-proposal-automation.git

2. 의존성 설치:
   pip install -r requirements.txt

3. 실행:
   streamlit run app.py

4. 브라우저에서 접속:
   http://localhost:8501

완전한 기능을 위해서는 로컬 설치를 권장합니다.`);
        }
    </script>
</body>
</html>
        """
        
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(html_content.encode('utf-8'))
        
    def do_POST(self):
        # Handle API requests
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        
        response = {
            "status": "success",
            "message": "Korean VC Proposal Automation Platform API",
            "version": "1.0",
            "features": [
                "2025 KIF GP selection optimization",
                "19 real sheet templates",
                "PDF parsing",
                "Excel generation",
                "Enterprise security"
            ]
        }
        
        self.wfile.write(json.dumps(response).encode('utf-8'))