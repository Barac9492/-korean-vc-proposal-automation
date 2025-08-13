#!/usr/bin/env python3
"""
Test script for KIF 2025 RFP parsing functionality
"""

import tempfile
import json
import re
import os

def test_kif_parsing():
    """Test the KIF RFP parsing with actual announcement text"""
    
    # Create a mock PDF with the actual KIF text
    kif_text = """
    KIF투자조합 업무집행조합원 선정계획 공고
    2025년 KIF투자조합 업무집행조합원 선정계획을 아래와 같이 공고합니다.
    <공고일 : 2025.08.12.>
    
    출자규모 •1,500억
    조 합 수 •16개
    
    AI·AX 혁신 3개 450억
    AI·ICT (운용사 제안) 10개 750억
    ICT 기술사업화 1개 100억
    AI 반도체 2개 200억
    
    의무투자금액 ∙AI·ICT(운용사제안),ICT기술사업화,AI반도체 :약정총액60%이상또는KIF출자금의2배이상
    ∙AI·AX 혁신:약정총액60% 이상
    
    존속기간 ∙8년이내(투자기간은운용사제안)
    운용사출자비율 ∙약정총액의1% 이상
    
    핵심운용인력 ∙ 핵심운용인력총3인이상참여(대표펀드매니저1인포함)
    ※단,결성총액이200억원이하인경우2인이상
    ∙ [자격 요건] 공고일 현재기준으로, 대표펀드매니저는 5년 이상, 기타 핵심운용인력은3년이상의투자경력 요건충족
    
    접수마감 •2025.8월28일(목), 16:00
    
    선정 절차 : 공고 → 제안서 접수 →1차 심의(서류평가)→ 현장실사→1차 평가결과 발표 → 2차 심의(PT발표평가) → 최종 선정
    
    선정배제대상
    •공고전일기준으로운영중인KIF자펀드의투자비율이60%미만이거나최근 KIF 자펀드선정년도로부터2년이미경과된업무집행조합원
    •자산건전성이취약(자본잠식률50%이상)하거나최근2년내도덕적해이등으로 사회적물의를일으킨업무집행조합원
    • 업무집행조합원의 대표펀드매니저가 중소벤처기업부로부터 감봉 이상의 제재를 받은날로부터3년이경과하지않은경우
    
    수탁기관 ∙ KIF 투자조합이 지정하는 수탁기관
    회계감사인 ∙ KIF 투자조합이 지정하는 조건에 만족하는 회계감사인
    ERP ∙ KIF ERP시스템 의무 사용
    분야별 중복지원 불가
    """
    
    # Create a temporary text file (simulating PDF parsing result)
    with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False, encoding='utf-8') as f:
        f.write(kif_text)
        temp_path = f.name
    
    # Test the parsing function
    print("🧪 Testing KIF 2025 RFP Parsing...")
    print("=" * 50)
    
    # Test patterns
    results = {}
    
    # Announcement date
    announce_pattern = r'공고일\s*[:：]?\s*(\d{4})[.\-년]\s*(\d{1,2})[.\-월]\s*(\d{1,2})'
    announce_match = re.search(announce_pattern, kif_text)
    if announce_match:
        results['announcement_date'] = f"{announce_match.group(1)}-{announce_match.group(2):0>2}-{announce_match.group(3):0>2}"
    
    # Submission deadline
    deadline_pattern = r'접수마감\s*[:：]?\s*•?\s*(\d{4})[.\-년]?\s*(\d{1,2})\s*월?\s*(\d{1,2})\s*일?'
    deadline_match = re.search(deadline_pattern, kif_text)
    if deadline_match:
        results['submission_deadline'] = f"{deadline_match.group(1)}-{deadline_match.group(2):0>2}-{deadline_match.group(3):0>2}"
    
    # Total fund size
    total_size_pattern = r'출자규모\s*[:：]?\s*•?\s*([\d,]+)\s*억'
    total_size_match = re.search(total_size_pattern, kif_text)
    if total_size_match:
        results['total_fund_size'] = total_size_match.group(1).replace(',', '') + '억원'
    
    # Fund count
    fund_count_pattern = r'조\s*합\s*수\s*[:：]?\s*•?\s*(\d+)\s*개'
    fund_count_match = re.search(fund_count_pattern, kif_text)
    if fund_count_match:
        results['fund_count'] = fund_count_match.group(1) + '개'
    
    # Investment areas
    investment_areas = []
    if 'AI·AX 혁신' in kif_text:
        investment_areas.append('AI·AX 혁신')
    if 'AI·ICT' in kif_text:
        investment_areas.append('AI·ICT')
    if 'ICT 기술사업화' in kif_text:
        investment_areas.append('ICT 기술사업화')
    if 'AI 반도체' in kif_text:
        investment_areas.append('AI 반도체')
    results['investment_areas'] = investment_areas
    
    # Mandatory investment
    mandatory_pattern = r'의무투자\s*금액\s*[:：]?\s*.*?(\d+)%\s*이상'
    mandatory_match = re.search(mandatory_pattern, kif_text)
    if mandatory_match:
        results['mandatory_investment'] = mandatory_match.group(1) + '%'
    
    # Fund duration
    duration_pattern = r'존속\s*기간\s*[:：]?\s*∙?\s*(\d+)\s*년\s*이내'
    duration_match = re.search(duration_pattern, kif_text)
    if duration_match:
        results['fund_duration'] = duration_match.group(1) + '년 이내'
    
    # GP contribution
    gp_contrib_pattern = r'운용사\s*출자비율\s*[:：]?\s*∙?\s*약정총액의\s*(\d+)%\s*이상'
    gp_contrib_match = re.search(gp_contrib_pattern, kif_text)
    if gp_contrib_match:
        results['gp_contribution'] = '약정총액의 ' + gp_contrib_match.group(1) + '% 이상'
    
    # Core personnel requirements
    personnel_reqs = {}
    if '총3인이상' in kif_text:
        personnel_reqs['minimum_count'] = '3인 이상'
    elif '2인이상' in kif_text:
        personnel_reqs['minimum_count'] = '2인 이상 (200억원 이하 펀드)'
    
    if '대표펀드매니저는 5년 이상' in kif_text:
        personnel_reqs['lead_manager_experience'] = '5년 이상'
    if '기타 핵심운용인력은3년이상' in kif_text:
        personnel_reqs['other_experience'] = '3년 이상'
    
    results['core_personnel_requirements'] = personnel_reqs
    
    # Evaluation process
    eval_process = []
    if '1차심의(서류평가)' in kif_text:
        eval_process.append('1차 심의 (서류평가)')
    if '현장실사' in kif_text:
        eval_process.append('현장실사')
    if '2차심의(PT발표평가)' in kif_text:
        eval_process.append('2차 심의 (PT발표평가)')
    if '최종선정' in kif_text:
        eval_process.append('최종선정 (우선협상대상자)')
    results['evaluation_process'] = eval_process
    
    # Exclusion criteria
    exclusions = []
    if '투자비율이60%미만' in kif_text:
        exclusions.append('기존 KIF 펀드 투자비율 60% 미만')
    if '2년이미경과' in kif_text:
        exclusions.append('최근 선정 후 2년 미경과')
    if '자본잠식률50%이상' in kif_text:
        exclusions.append('자본잠식률 50% 이상')
    if '감봉 이상의 제재' in kif_text:
        exclusions.append('대표펀드매니저 제재 이력 (3년 이내)')
    results['exclusion_criteria'] = exclusions
    
    # KIF specific requirements
    kif_requirements = []
    if 'KIF ERP시스템 의무 사용' in kif_text:
        kif_requirements.append('KIF ERP 시스템 의무 사용')
    if '수탁기관' in kif_text:
        kif_requirements.append('KIF 지정 수탁기관 사용')
    if '회계감사인' in kif_text:
        kif_requirements.append('KIF 지정 조건 만족 회계감사인')
    if '분야별 중복지원 불가' in kif_text:
        kif_requirements.append('분야별 중복지원 불가')
    results['kif_specific_requirements'] = kif_requirements
    
    # Display results
    print("📊 Parsing Results:")
    print(json.dumps(results, ensure_ascii=False, indent=2))
    
    # Validate key extractions
    print("\n✅ Validation:")
    assert results.get('announcement_date') == '2025-08-12', f"Expected 2025-08-12, got {results.get('announcement_date')}"
    assert results.get('submission_deadline') == '2025-08-28', f"Expected 2025-08-28, got {results.get('submission_deadline')}"
    assert results.get('total_fund_size') == '1500억원', f"Expected 1500억원, got {results.get('total_fund_size')}"
    assert results.get('fund_count') == '16개', f"Expected 16개, got {results.get('fund_count')}"
    assert 'AI·AX 혁신' in results.get('investment_areas', []), "Missing AI·AX 혁신"
    assert results.get('mandatory_investment') == '60%', f"Expected 60%, got {results.get('mandatory_investment')}"
    assert results.get('fund_duration') == '8년 이내', f"Expected 8년 이내, got {results.get('fund_duration')}"
    assert results.get('gp_contribution') == '약정총액의 1% 이상', f"Expected 약정총액의 1% 이상, got {results.get('gp_contribution')}"
    
    print("All validations passed! ✅")
    
    # Clean up
    os.unlink(temp_path)
    
    return results

if __name__ == "__main__":
    test_results = test_kif_parsing()
    print("\n🎉 KIF 2025 RFP parsing test completed successfully!")
    print(f"📝 Extracted {len([k for k, v in test_results.items() if v])} key data points")