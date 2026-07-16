
const initial_velocity = document.querySelector('#myTextBox')

initial_velocity.addEventListener('keydown', function(event) {

    if (event.key === 'Enter') {
        event.preventDefault();

        console.log("Button pressed: ", initial_velocity);
    }

});