// Day 15: Quiz App
const questions = [
    { question: "What does HTML stand for?", answers: ["Hyper Text Markup Language", "High Tech Modern Language", "Home Tool Markup Language", "Hyperlinks Text Mark Language"], correct: 0 },
    { question: "Which CSS property changes text color?", answers: ["font-color", "text-color", "color", "foreground"], correct: 2 },
    { question: "What does console.log() do?", answers: ["Creates a popup", "Prints to console", "Saves to file", "Sends an email"], correct: 1 },
    { question: "Which symbol is used for Python comments?", answers: ["//", "/* */", "#", "--"], correct: 2 },
    { question: "What does API stand for?", answers: ["Application Programming Interface", "Advanced Program Integration", "Automated Processing Input", "App Process Integration"], correct: 0 },
    { question: "What does CSS stand for?", answers: ["Computer Style Sheets", "Cascading Style Sheets", "Creative Style System", "Colorful Style Sheets"], correct: 1 },
    { question: "Which is NOT a JavaScript data type?", answers: ["string", "boolean", "float", "undefined"], correct: 2 },
    { question: "What does JSON stand for?", answers: ["JavaScript Object Notation", "Java Standard Object Notation", "JavaScript Online Notation", "Java Syntax Object Naming"], correct: 0 },
    { question: "Which HTTP method retrieves data?", answers: ["POST", "PUT", "GET", "DELETE"], correct: 2 },
    { question: "What status code means 'Not Found'?", answers: ["200", "301", "404", "500"], correct: 2 }
];

let currentQuestion = 0;
let score = 0;
let timeLeft = 30;
let timerInterval = null;
let userAnswers = [];

// DOM Elements
const startScreen = document.getElementById('start-screen');
const quizScreen = document.getElementById('quiz-screen');
const resultsScreen = document.getElementById('results-screen');
const startBtn = document.getElementById('start-btn');
const restartBtn = document.getElementById('restart-btn');
const questionEl = document.getElementById('question');
const answersEl = document.getElementById('answers');
const progressEl = document.getElementById('progress');
const timerEl = document.getElementById('timer');
const scoreEl = document.getElementById('score');
const progressFill = document.getElementById('progress-fill');

function startQuiz() {
    // TODO: Reset state, hide start screen, show quiz screen, load first question
}

function showQuestion() {
    // TODO: Display question, create answer buttons, update progress, start timer
}

function startTimer() {
    // TODO: Countdown from 30, update display, change color when low, auto-advance at 0
}

function selectAnswer(selectedIndex) {
    // TODO: Stop timer, check answer, show feedback, wait 1.5s, next question
}

function nextQuestion() {
    // TODO: Advance or show results
}

function showResults() {
    // TODO: Show final score, percentage, review
}

// TODO: Event listeners for start, restart, answer clicks (event delegation)
