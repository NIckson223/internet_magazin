function validateInput(input) {
      input.value = input.value.replace(/\D/g, '');
      if (input.value < 1) {
        input.value = 1;
      }
    }

function increment() {
    var input = document.getElementById('quantity');
    input.value = parseInt(input.value, 10) + 1;
    validateInput(input);
    }

function decrement() {
    var input = document.getElementById('quantity');
    input.value = Math.max(1, parseInt(input.value, 10) - 1);
    validateInput(input);
    }