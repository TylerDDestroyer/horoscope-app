from flask import Flask, render_template, request
from datetime import datetime
import requests


app = Flask(__name__)

def get_zodiac_sign(month, day):
    if (month == 3 and day >= 12) or (month == 4 and day <= 19):
        return "ARIES (Mar 21 - Apr 20) Embrace the new year with positivity and good vibes. This is the year to expect sudden financial gains and create multiple income streams. Minimize unnecessary spending, and invest wisely to achieve your financial goals. Lucky Number: 1 Lucky Colour: Yellow Lucky Months: January, August & October."
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
        return "TAURUS (Apr 21-May 20) Welcome 2024 with a smile as it unfolds a myriad of opportunities and unexpected triumphs.While prospects to accumulate wealth may arise, the possibility of heavy expenditure lingers too. Exercise caution when lending money. Research, plan and adapt your strategies as and when needed, but remain open to new, unconventional ideas on the business front. Lucky Number: 9 Lucky Colour: Green Lucky Months: April, September & December."
    elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
        return "GEMINI (May 21 - Jun 21) Gemini, let us put the past behind and start afresh in the year 2024. Business ventures are likely to thrive in the first two quarters, and your diligence will be rewarded with unexpected monetary gains.You are advised to stay away from get-quick-rich schemes and should prioritize savings throughout the year."
    elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
        return "CANCER (Jun 22 - Jul 22) This year promises to be an eventful one for Cancerians. Your income potential is poised for a notable boost. A balanced approach between work and family responsibilities will make the life magical.Investing in improving money markets and strategizing savings side by side will highlight the financial front. Those who feel stuck in their careers will receive new offers aligning with their future. Lucky Number: 2 Lucky Colour: Orange Lucky Months: January, March & September."
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
        return "LEO (Jul 23 - Aug 23) In 2024, Leo will continue to radiate energy and enthusiasm, propelling them towards their goal. Businesses, especially in financial services, infrastructure, hospitality and international trade are set for profit surges.Lucky Number: 5 Lucky Colour: Golden Lucky Months: March & July. "
    elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
        return "VIRGO (Aug 24 - Sept 23) For Virgos, caution is the name of the game in 2024, both in personal and professional spheres. Financial stability is foreseen all year long. Some of you may remain spiritually active.Be wary of unexpected reversals in the second or third quarters that may nullify past gains, and guard yourself against deception from associates during important business deals. Lucky Number: 6 Lucky Colour: Brown Lucky Months: June, September & December."
    elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
        return "LIBRA (Sept 24 - Oct 23) An exhilarating journey awaits you in 2024! Brace yourself for the strengthening of business ties that usher in an upswing in earnings.  But be cautious, for post-May, a surge in expenditure looms as a possibility. Cultivate a special place in the hearts of your loved ones through gestures of kindness. Lucky Number: 4 Lucky Colour: Green Lucky Months: February, April & May"
    elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
        return "SCORPIO (Oct 24 - Nov 22) A wave of positivity awaits all Scorpios in 2024! The year unfolds positively on the financial front, offering a promising landscape for investment in shares and speculative activities. However, businessmen need to be careful in the months of February and June. Unity within your family is set to strengthen, allowing you to foster a harmonious balance between personal and professional commitments.Lucky Number: 9 Lucky Colour: Red Lucky Months: March, May & August."
    elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
        return "SAGITARIUS (Nov 23 - Dec 21) “Change” is going to be your mantra in 2024. It’s time to address delayed tasks and resolve lingering differences. Anticipate new adventures to elevate your joy, as unexpected yet positive experiences await you in your business ventures. Success is in store for those appearing for competitive exams or trying their luck for a government job. Expect a blend of challenges and triumphs in your career, and resist unproductive temptations to stay on course. Lucky Number: 5 Lucky Colour: Pink Lucky Months: May, July & December."
    elif (month == 12 and day >= 22) or (month == 1 and day <= 19):
        return "CAPRICORN (Dec 22 - Jan 21) 2024 is likely to bring with itself an opportune time. Embrace a penchant for calculated risks this year, as entrepreneurial spirits are likely to be rewarded. With financial gains, you also have a freedom to buy things you have been longing for. Focus on strengthening family bonds and make sure your marital bond is not affected by what others say.Maintaining a positive attitude would be the key to your success. Time management would be important for students to achieve their goals on the academic front. Lucky Number: 8 Lucky Colour: Grey Lucky Months: February, May & October."
    elif (month == 1 and day >= 20) or (month == 2 and day <= 18):
        return "AQUARIUS (Jan 22 - Feb 19) You can look forward to a fruitful year, Aquarius! You can anticipate skyrocketing success and material abundance with the onset of 2024.Embrace saving and financial planning as business may experience stagnation in the third quarter. Astute expense management and minute supervision would also be required in that phase. Your career stands on the brink of success, offering you significant achievements and opportunities that you have been desperately looking forward to. Lucky Number: 7 Lucky Colour: Peach Lucky Months: May & June."
    elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
        return "PISCES (Feb 20 - Mar 20) Welcome 2024 with a smile as many important developments are in store for you this year. For those eyeing business growth, this is an opportune year! With increased earnings, expect a rise in expenses as well. To combat this, master the art of saving and investing strategically.Heal old wounds with long-lost family connections and foster healthier relationships with those around you. Expect a topsy-turvy experience in regards to health, as most eye or foot-related ailments may make you look for medical guidance. Lucky Number: 6 Lucky Colour: Yellow Lucky Months: March, April & November."
    else:
        return ""
         
@app.route('/')
def render():
    current_date = datetime.now()
    show_date = current_date.strftime("%B %d, %Y")
    return render_template('index.html', show_date=show_date)
   

@app.route('/get_horoscope', methods=['POST'])
def get_horoscope():
        birth_date = request.form["birthday"]
        birth_year, birth_month, birth_day = map(int, birth_date.split("-"))
        zodiac_sign = get_zodiac_sign(birth_month, birth_day)
        return render_template('index.html', zodiac_sign=zodiac_sign)

if __name__ == '__main__':
    app.run(debug=True)