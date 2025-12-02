from django.shortcuts import render

# Question class
class Questions:
    def __init__(self, que, a, b, c, d, correct):
        self.que = que
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.correct = correct  # answer: 'a', 'b', 'c', 'd'

def testpaper(request):
    questions = [
        Questions('मोमबत्ती पिघलना किस प्रकार का परिवर्तन है?',
                  '(a) रासायनिक परिवर्तन', '(b) भौतिक परिवर्तन', '(c) दोनों', '(d) इनमें से कोई नहीं', 'b'),

        Questions('कागज़ जलना किस प्रकार का परिवर्तन है?',
                  '(a) भौतिक परिवर्तन', '(b) रासायनिक परिवर्तन', '(c) दोनों', '(d) कोई नहीं', 'b'),

        Questions('पानी का भाप में बदलना एक—',
                  '(a) भौतिक परिवर्तन', '(b) रासायनिक परिवर्तन', '(c) अपचयन', '(d) संलेषण', 'a'),

        Questions('लोहे पर जंग लगना है—',
                  '(a) भौतिक परिवर्तन', '(b) रासायनिक परिवर्तन', '(c) कोई नहीं', '(d) दोनों', 'b'),

        Questions('चीनी को पानी में घोलना—',
                  '(a) भौतिक परिवर्तन', '(b) रासायनिक परिवर्तन', '(c) दोनों', '(d) कोई नहीं', 'a'),

        Questions('दही जमना किस प्रकार का परिवर्तन है?',
                  '(a) भौतिक', '(b) रासायनिक', '(c) दोनों', '(d) कोई नहीं', 'b'),

        Questions('बर्फ का पानी बनना—',
                  '(a) दोनों परिवर्तन', '(b) रासायनिक परिवर्तन', '(c) भौतिक परिवर्तन', '(d) इनमें से कोई नहीं', 'c'),

        Questions('कोयला जलना किस प्रकार का परिवर्तन है?',
                  '(a) भौतिक', '(b) रासायनिक', '(c) दोनों', '(d) कोई नहीं', 'b'),

        Questions('दूध का फटना किस प्रकार का परिवर्तन है?',
                  '(a) भौतिक', '(b) रासायनिक', '(c) दोनों', '(d) कोई नहीं', 'b'),

        Questions('कांच का टूटना—',
                  '(a) भौतिक परिवर्तन', '(b) रासायनिक परिवर्तन', '(c) अपघटन', '(d) संश्लेषण', 'a'),
    ]

    # If student submits the test
    if request.method == "POST":
        score = 0
        detailed_result = []

        for i, q in enumerate(questions, 1):
            selected_option = request.POST.get(f'option{i}')  # user's selected option

            # Score increase
            if selected_option == q.correct:
                score += 1

            # Store detailed question review
            detailed_result.append({
                'question': q.que,
                'options': [q.a, q.b, q.c, q.d],
                'correct': q.correct,
                'selected': selected_option
            })

        total = len(questions)
        percentage = round((score / total) * 100, 1)

        context = {
            'score': score,
            'total': total,
            'percentage': percentage,
            'result': detailed_result
        }
        return render(request, 'result.html', context)

    # First time load
    return render(request, 'question.html', {'questions': questions})
