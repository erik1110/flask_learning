from flask import Flask, render_template

app = Flask(__name__)

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/history')
def page_history():
    return render_template('history.html')

@app.route('/member')
def page_member():
    context = {
        'person1': {'name': '炭治郎'',
                    'age': 15,
                    'birthday': '0714',
                    'interest': '頭槌、掃除、幫助有難人',
                    'image':'images/person1.jpg',
                   },
        'person2': {'name': '禰豆子',
                    'age': 14,
                    'birthday': '1228',
                    'interest': '縫紉',
                    'image':'images/person2.jpg',                   
                   },
        'person3': {'name': '善逸',
                    'age': 16,
                    'birthday': '0903'',
                    'interest': '把妹',
                    'image':'images/person3.jpg',                   
                   },
        'person4': {'name': '伊之助',
                    'age': 15,
                    'birthday': '0422',
                    'interest': '嘴砲',
                    'image':'images/person4.jpg',
                   },
        'person5': {'name': '香奈乎',
                    'age': 16,
                    'birthday': '0519',
                    'interest': '躑硬幣',
                    'image':'images/person5.jpg',
                   },
    }
    return render_template('member.html', context=context)

@app.route('/admission')
def page_admission():
    return render_template('admission.html')

@app.route('/information')
def page_information():
    return render_template('information.html')

if __name__ == "__main__":
    app.run(debug=True)