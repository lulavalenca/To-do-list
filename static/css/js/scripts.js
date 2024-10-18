// Function to mark a todo as completed
function toggleComplete(todoElement) {
    todoElement.classList.toggle('completed');
}

// Function to confirm deletion of a todo
function confirmDelete(event) {
    const confirmation = confirm("Are you sure you want to delete this task?");
    if (!confirmation) {
        event.preventDefault(); // Prevent the default action if not confirmed
    }
}

// Attach event listeners to todo items and delete links
document.addEventListener('DOMContentLoaded', () => {
    const todoItems = document.querySelectorAll('li');

    todoItems.forEach(item => {
        item.addEventListener('click', () => toggleComplete(item)); // Toggle complete on click

        const deleteLink = item.querySelector('a');
        if (deleteLink) {
            deleteLink.addEventListener('click', confirmDelete); // Confirm delete
        }
    });
});