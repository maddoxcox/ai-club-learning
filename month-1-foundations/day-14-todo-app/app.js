// Day 14: Todo List App
let todos = [];
let currentFilter = 'all';

const todoInput = document.getElementById('todo-input');
const addBtn = document.getElementById('add-btn');
const todoList = document.getElementById('todo-list');
const itemsLeft = document.getElementById('items-left');
const clearCompletedBtn = document.getElementById('clear-completed');
const filterBtns = document.querySelectorAll('.filter-btn');

function addTodo() {
    // TODO: Get text, create todo object {id, text, completed}, add to array, render, save
}

function toggleTodo(id) {
    // TODO: Toggle completed status, render, save
}

function deleteTodo(id) {
    // TODO: Remove from array, render, save
}

function renderTodos() {
    // TODO: Clear list, filter by currentFilter, create DOM elements for each todo
    // Each todo: li > [checkbox, span.todo-text, button.delete-btn]
    // Update items left counter
}

function setFilter(filter) {
    // TODO: Update currentFilter, update active button class, render
}

function clearCompleted() {
    // TODO: Remove completed todos, render, save
}

function saveTodos() {
    // TODO: localStorage.setItem with JSON.stringify
}

function loadTodos() {
    // TODO: localStorage.getItem and JSON.parse
}

// TODO: Add event listeners for addBtn, input Enter key, filter buttons, clear completed
// TODO: Use event delegation on todoList for checkbox and delete

// Initialize
loadTodos();
renderTodos();
