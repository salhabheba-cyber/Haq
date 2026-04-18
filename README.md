# 🛡️ Haq - اعرف الحَقّ قبل ما تندم

**🇱🇧 Built in Beirut, Lebanon**

## What is Haq?
Haq helps you detect scam messages on WhatsApp, SMS, and phone calls.

## Features
- 📱 WhatsApp message scanner
- ✉️ SMS spam detector
- 📞 Phone number checker
- 🌍 Bilingual reports (Arabic/English)
- 📊 Admin dashboard

## Objective
Build an OSINT investigation tool to detect scam messages and phone numbers across multiple platforms.

## Key Skills Demonstrated
- OSINT techniques for phone/email/username investigation
- API integration (Truecaller, VirusTotal)
- Database management for spam reports
- Bilingual report generation (Arabic/English)

## My Process
1. **Data Collection**: Gathered spam patterns and scam indicators
2. **API Integration**: Connected to Truecaller and VirusTotal APIs
3. **Analysis Engine**: Built detection logic using keyword matching and URL scanning
4. **Reporting**: Generated bilingual reports in PDF and JSON formats

## Tools Used
- Python, Requests, JSON
- SQLite, Streamlit
- Truecaller API, VirusTotal API

## Key Takeaways
- OSINT is critical for threat intelligence
- Crowdsourced spam data improves detection accuracy
- Bilingual support expands user base

## Live Demo
👉 [https://haq.streamlit.app](https://haq.streamlit.app)

## Run Locally
```bash
git clone https://github.com/salhabheba-cyber/Haq.git
cd Haq
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
streamlit run web/app.py


