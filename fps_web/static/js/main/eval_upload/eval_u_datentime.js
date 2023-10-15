function updateDateTime() {
    const now = new Date();
    const timeElement = document.getElementById('evalBreadtime');
    const dateElement = document.getElementById('evalBreaddate');

    const options = {
        hour: 'numeric',
        minute: 'numeric',
        second: 'numeric',
        hour12: true
    };

    timeElement.textContent = now.toLocaleTimeString(undefined, options);
    dateElement.textContent = now.toDateString();

    const currentHour = now.getHours();
}
setInterval(updateDateTime, 1000);
updateDateTime();