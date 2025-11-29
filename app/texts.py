# app/texts.py

TEXTS = {
    "en": {
        "welcome_card": (
            "SafeSathi में आपका स्वागत है!\n\n"
            "क्या आपको साइबर मुद्दों में मदद चाहिए?\n"
            "आप सही जगह पर हैं! SafeSathi आपकी मदद के लिए यहाँ है।\n"
            "साइबर अपराध की रिपोर्ट करने से लेकर सुरक्षा सुझाव प्राप्त करने तक, हम आपके साथ हैं।\n\n"
            "शुरू करने के लिए भाषा चुनें"
        ),
        "welcome_after_lang": (
            "Welcome to SafeSathi! 🛡️\n"
            "How can I assist you today?"
        ),
        "menu": (
            "✅ Main Menu:\n"
            "1. Check Suspicious Link\n"
            "2. Check Message\n"
            "3. Daily Cyber Tip\n"
            "4. Report a Scam\n"
            "5. Latest Scam Alerts\n"
            "6. Awareness Blog\n"
            "7. Safety Checklist\n"
            "8. Scam Reporting Sites\n"
            "9. Exit"
        ),
        "report_init": "😟 I'm sorry to hear that. Please briefly describe what happened so I can guide you better.\n(Example: 'I lost money in a task scam' or 'Someone is blackmailing me')",
        "report_fallback": (
            "Thank you for sharing. Here is what you should do immediately:\n\n"
            "1. **Call 1930** (National Cyber Crime Helpline).\n"
            "2. File a complaint at **https://cybercrime.gov.in**.\n"
            "3. If money was deducted, contact your bank immediately to freeze the transaction.\n\n"
            "Stay calm and do not delete any chats or screenshots."
        ),
        "awaiting_link": "🔗 Please paste the suspicious link you'd like me to check.",
        "awaiting_report": "📩 Please paste the scam message or suspicious text:",
        "scan_result": "🔍 Scan Result:\nLink: {url}\nStatus: **{label}** (confidence {prob:.2f})",
        "scam_result": "📝 Scam Message Scan:\nStatus: **{label}** (confidence {prob:.2f})",
        "tip": (
            "💡 **Cyber Tip:** Never share your OTP or UPI PIN with anyone.\n"
            "Bank officials will NEVER ask for this information."
        ),
        "return_menu": "\n\nType 'menu' to return.",
        "unknown": "I didn't understand that. Type 'menu' to see options.",
        "safe": "SAFE",
        "suspicious": "SUSPICIOUS",
        "scam": "SCAM",
        "not_scam": "SAFE",
        "alerts": "🚨 **Latest Alerts:**\n- Fake electricity bill SMS scam is rising.\n- Beware of 'Work from Home' task scams on Telegram.",
        "blog": "📚 Read our latest awareness blog here: [SafeSathi Blog](#)",
        "checklist": "✅ **Safety Checklist:**\n1. Strong passwords?\n2. 2FA enabled?\n3. Antivirus updated?",
        "reporting_sites": "🔗 **Official Reporting:**\n- https://cybercrime.gov.in\n- https://sancharsaathi.gov.in",
        "exit": "👋 Stay safe! Type 'hi' to start again.",
        "scam_detected_footer": (
            "⚠️ **This looks like a scam.**\n"
            "Do not reply or click links.\n"
            "📞 Report to 1930 or https://cybercrime.gov.in"
        ),
        "safe_footer": "✅ This message looks safe, but always verify the sender.",
        "helpline": (
            "📞 Cybercrime Helpline: Call 1930\n"
            "Portal: https://www.cybercrime.gov.in\n"
            "Sanchar Sathi: https://sancharsaathi.gov.in"
        ),
        "menu_select_prompt": "\n\nकृपया चुनें कि आपके लिए क्या सबसे उपयुक्त है:",
        "did_you_mean": "💡 **Did you mean:** {suggestion}?",
        "typo_format": "(The link you entered has a typo or unusual format.)",
        "http_insecure": "(You used 'http' which is unsecure. 'https' is safer.)",
        "http_risk": "⚠️ **Risk:** Unencrypted Connection (HTTP).\nThis site is not secure. Attackers can steal data you send here.",
        "risk_warning": "⚠️ This may be risky. Be careful with unknown links or messages, especially if they ask for OTP, bank details, or urgent payments. Verify using official apps or websites instead of clicking directly."
    },
    "hi": {
        "welcome_card": (
            "Welcome to **SafeSathi Cyber Crime Help Assistant!** 🛡️\n\n"
            "Need help with cyber issues? 🔍\n"
            "You are in the right place! SafeSathi is here to guide you quickly and effectively.\n"
            "From reporting cybercrimes to getting safety tips, you are covered.\n\n"
            "**Select Language to begin! 💬**"
        ),
        "welcome_after_lang": (
            "SafeSathi में आपका स्वागत है! 🛡️\n"
            "आपको किस प्रकार की सहायता चाहिए?"
        ),
        "menu": (
            "✅ मुख्य मेनू:\n"
            "1. संदिग्ध लिंक की जाँच करें\n"
            "2. संदेश की जाँच करें\n"
            "3. दैनिक साइबर सुरक्षा सुझाव\n"
            "4. स्कैम की रिपोर्ट करें\n"
            "5. नवीनतम स्कैम अलर्ट\n"
            "6. जागरूकता ब्लॉग\n"
            "7. सुरक्षा चेकलिस्ट\n"
            "8. स्कैम रिपोर्टिंग साइटें\n"
            "9. बाहर निकलें"
        ),
        "report_init": "😟 यह सुनकर दुख हुआ। कृपया संक्षेप में बताएं कि क्या हुआ ताकि मैं आपकी बेहतर मदद कर सकूं।\n(उदाहरण: 'मैंने टास्क स्कैम में पैसे खो दिए' या 'कोई मुझे ब्लैकमेल कर रहा है')",
        "report_fallback": (
            "साझा करने के लिए धन्यवाद। यहाँ आपको तुरंत क्या करना चाहिए:\n\n"
            "1. **1930 पर कॉल करें** (राष्ट्रीय साइबर अपराध हेल्पलाइन)।\n"
            "2. **https://cybercrime.gov.in** पर शिकायत दर्ज करें।\n"
            "3. यदि पैसे कट गए हैं, तो लेनदेन को फ्रीज करने के लिए तुरंत अपने बैंक से संपर्क करें।\n\n"
            "शांत रहें और कोई भी चैट या स्क्रीनशॉट न हटाएं।"
        ),
        "awaiting_link": "🔗 कृपया वह संदिग्ध लिंक पेस्ट करें जिसकी आप जाँच करना चाहते हैं।",
        "awaiting_report": "📩 कृपया स्कैम संदेश या संदिग्ध टेक्स्ट पेस्ट करें:",
        "scan_result": "🔍 स्कैन परिणाम:\nलिंक: {url}\nस्थिति: **{label}** (विश्वास {prob:.2f})",
        "scam_result": "📝 स्कैम संदेश स्कैन:\nस्थिति: **{label}** (विश्वास {prob:.2f})",
        "tip": (
            "💡 **साइबर सुझाव:** अपना OTP या UPI पिन किसी के साथ साझा न करें।\n"
            "बैंक अधिकारी कभी भी यह जानकारी नहीं मांगेंगे।"
        ),
        "return_menu": "\n\nवापस जाने के लिए 'menu' टाइप करें।",
        "unknown": "मुझे समझ नहीं आया। विकल्प देखने के लिए 'menu' टाइप करें।",
        "safe": "सुरक्षित",
        "suspicious": "संदिग्ध",
        "scam": "स्कैम",
        "not_scam": "सुरक्षित",
        "alerts": "🚨 **नवीनतम अलर्ट:**\n- बिजली बिल के फर्जी एसएमएस स्कैम बढ़ रहे हैं।\n- टेलीग्राम पर 'वर्क फ्रॉम होम' टास्क स्कैम से सावधान रहें।",
        "blog": "📚 हमारा नवीनतम जागरूकता ब्लॉग यहाँ पढ़ें: [SafeSathi Blog](#)",
        "checklist": "✅ **सुरक्षा चेकलिस्ट:**\n1. मजबूत पासवर्ड?\n2. 2FA सक्षम?\n3. एंटीवायरस अपडेट?",
        "reporting_sites": "🔗 **आधिकारिक रिपोर्टिंग:**\n- https://cybercrime.gov.in\n- https://sancharsaathi.gov.in",
        "exit": "👋 सुरक्षित रहें! फिर से शुरू करने के लिए 'hi' टाइप करें।",
        "scam_detected_footer": (
            "⚠️ **यह एक स्कैम लग रहा है।**\n"
            "जवाब न दें और लिंक पर क्लिक न करें।\n"
            "📞 1930 या https://cybercrime.gov.in पर रिपोर्ट करें"
        ),
        "safe_footer": "✅ यह संदेश सुरक्षित लग रहा है, लेकिन हमेशा प्रेषक की जाँच करें।",
        "helpline": (
            "📞 साइबर अपराध हेल्पलाइन: 1930 पर कॉल करें\n"
            "पोर्टल: https://www.cybercrime.gov.in\n"
            "संचार साथी: https://sancharsaathi.gov.in"
        ),
        "menu_select_prompt": "\n\nकृपया चुनें कि आपके लिए क्या सबसे उपयुक्त है:",
        "did_you_mean": "💡 **क्या आपका मतलब था:** {suggestion}?",
        "typo_format": "(आपके द्वारा दर्ज किए गए लिंक में टाइपो या असामान्य प्रारूप है।)",
        "http_insecure": "(आपने 'http' का उपयोग किया जो असुरक्षित है। 'https' अधिक सुरक्षित है।)",
        "http_risk": "⚠️ **जोखिम:** असुरक्षित कनेक्शन (HTTP)।\nयह साइट सुरक्षित नहीं है। हमलावर यहां भेजे गए डेटा को चुरा सकते हैं।",
        "risk_warning": "⚠️ यह जोखिमभरा हो सकता है। अज्ञात लिंक या संदेशों से सावधान रहें, खासकर यदि वे OTP, बैंक विवरण, या तत्काल भुगतान मांगते हैं। सीधे क्लिक करने के बजाय आधिकारिक ऐप या वेबसाइट का उपयोग करके सत्यापित करें।"
    },
    "ur": {
        "welcome_card": (
            "Welcome to **SafeSathi Cyber Crime Help Assistant!** 🛡️\n\n"
            "Need help with cyber issues? 🔍\n"
            "You are in the right place! SafeSathi is here to guide you quickly and effectively.\n"
            "From reporting cybercrimes to getting safety tips, you are covered.\n\n"
            "**Select Language to begin! 💬**"
        ),
        "welcome_after_lang": (
            "SafeSathi میں خوش آمدید! 🛡️\n"
            "آپ کو کس قسم کی مدد چاہیے؟"
        ),
        "menu": (
            "✅ مین مینو:\n"
            "1. مشکوک لنک چیک کریں\n"
            "2. پیغام چیک کریں\n"
            "3. روزانہ سائبر ٹپ\n"
            "4. اسکام کی رپورٹ کریں\n"
            "5. تازہ ترین اسکام الرٹس\n"
            "6. آگاہی بلاگ\n"
            "7. حفاظتی چیک لسٹ\n"
            "8. اسکام رپورٹنگ سائٹس\n"
            "9. باہر نکلیں"
        ),
        "report_init": "😟 یہ سن کر افسوس ہوا۔ براہ کرم مختصراً بتائیں کہ کیا ہوا تاکہ میں آپ کی بہتر رہنمائی کر سکوں۔",
        "report_fallback": (
            "شیئر کرنے کا شکریہ۔ یہاں آپ کو فوری طور پر کیا کرنا چاہیے:\n\n"
            "1. **1930 پر کال کریں**۔\n"
            "2. **https://cybercrime.gov.in** پر شکایت درج کریں۔\n"
            "3. اگر پیسے کٹ گئے ہیں، تو فوراً اپنے بینک سے رابطہ کریں۔"
        ),
        "awaiting_link": "🔗 براہ کرم مشکوک لنک پیسٹ کریں۔",
        "awaiting_report": "📩 براہ کرم اسکام پیغام پیسٹ کریں:",
        "scan_result": "🔍 اسکین نتیجہ:\nلنک: {url}\nحیثیت: **{label}** (اعتماد {prob:.2f})",
        "scam_result": "📝 اسکام پیغام اسکین:\nحیثیت: **{label}** (اعتماد {prob:.2f})",
        "tip": "💡 **سائبر ٹپ:** اپنا OTP کسی کے ساتھ شیئر نہ کریں۔",
        "return_menu": "\n\nواپس جانے کے لیے 'menu' ٹائپ کریں۔",
        "unknown": "مجھے سمجھ نہیں آیا۔ 'menu' ٹائپ کریں۔",
        "safe": "محفوظ",
        "suspicious": "مشکوک",
        "scam": "اسکام",
        "not_scam": "محفوظ",
        "alerts": "🚨 **تازہ ترین الرٹس:**\n- جعلی بجلی بل اسکام۔",
        "blog": "📚 ہمارا بلاگ: [SafeSathi Blog](#)",
        "checklist": "✅ **حفاظتی چیک لسٹ:**\n1. مضبوط پاس ورڈ؟\n2. 2FA فعال؟",
        "reporting_sites": "🔗 **سرکاری رپورٹنگ:**\n- https://cybercrime.gov.in",
        "exit": "👋 محفوظ رہیں!",
        "scam_detected_footer": "⚠️ **یہ اسکام لگ رہا ہے۔**\n📞 1930 پر رپورٹ کریں",
        "safe_footer": "✅ یہ پیغام محفوظ لگ رہا ہے۔",
        "helpline": "📞 سائبر کرائم ہیلپ لائن: 1930",
        "menu_select_prompt": "\n\nبراہ کرم منتخب کریں کہ آپ کے لیے کیا سب سے موزوں ہے:",
        "did_you_mean": "💡 **کیا آپ کا مطلب تھا:** {suggestion}؟",
        "typo_format": "(آپ کے داخل کردہ لنک میں ٹائپو یا غیر معمولی فارمیٹ ہے۔)",
        "http_insecure": "(آپ نے 'http' استعمال کیا جو غیر محفوظ ہے۔ 'https' زیادہ محفوظ ہے۔)",
        "http_risk": "⚠️ **خطرہ:** غیر محفوظ کنکشن (HTTP)۔\nیہ سائٹ محفوظ نہیں ہے۔ حملہ آور یہاں بھیجے گئے ڈیٹا کو چرا سکتے ہیں۔",
        "risk_warning": "⚠️ یہ خطرناک ہو سکتا ہے۔ نامعلوم لنکس یا پیغامات سے محتاط رہیں، خاص طور پر اگر وہ OTP، بینک کی تفصیلات، یا فوری ادائیگی مانگتے ہیں۔ براہ راست کلک کرنے کے بجائے سرکاری ایپس یا ویب سائٹس کا استعمال کرتے ہوئے تصدیق کریں۔"
    }
}

# Fallback to English for missing keys in other languages
def get_text(lang, key, **kwargs):
    lang_dict = TEXTS.get(lang, TEXTS["en"])
    text = lang_dict.get(key, TEXTS["en"].get(key, ""))
    if kwargs:
        return text.format(**kwargs)
    return text
