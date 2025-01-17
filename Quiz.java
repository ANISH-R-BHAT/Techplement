package QuizClasses;

import java.util.ArrayList;
import java.util.List;

class Quiz {
    private final String title;
    private final List<Question> questions;

    public Quiz(String title) {
        this.title = title;
        this.questions = new ArrayList<>();
    }

    public String getTitle() {
        return title;
    }

    public List<Question> getQuestions() {
        return questions;
    }

    public void addQuestion(Question question) {
        questions.add(question);
    }
}
