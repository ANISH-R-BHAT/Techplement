package QuizClasses;

import java.util.List;

class Question {
    private final String textString;
    private final List<String> options;
    private final int correctOptionIndex;

    public Question(String text, List<String> options, int correctOptionIndex) {
        this.textString = text;
        this.options = options;
        this.correctOptionIndex = correctOptionIndex;
    }

    public String getText() {
        return textString;
    }

    public List<String> getOptions() {
        return options;
    }

    public int getCorrectOptionIndex() {
        return correctOptionIndex;
    }
}