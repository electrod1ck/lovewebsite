function formatPhoneNumber(input) {
    let value = input.value.replace(/\D/g, ''); // Удаляем все нецифровые символы

    // Убеждаемся, что номер начинается с 7
    if (!value.startsWith('7')) {
        value = '7' + value;  // Если не начинается, добавляем 7 в начало
    }


    if (value.length > 11) {
        value = value.slice(0, 11);
    }

    let formattedNumber = '+7';

    if (value.length > 1) { // Начинаем форматировать, если есть хотя бы одна цифра после 7
        formattedNumber += ' (' + value.substring(1, 4);
    }

    if (value.length > 4) {
        formattedNumber += ') ' + value.substring(4, 7);
    }

    if (value.length > 7) {
        formattedNumber += '-' + value.substring(7, 9);
    }

    if (value.length > 9) {
        formattedNumber += '-' + value.substring(9, 11);
    }

    input.value = formattedNumber;
}

// Добавляем автоматический "+7" при загрузке страницы и при потере фокуса
document.addEventListener("DOMContentLoaded", function() {
    const phoneInput = document.querySelector('input[name="username"]'); // Ищем input по имени username
    if (phoneInput && phoneInput.value === "") {
        phoneInput.value = "+7";
    }
});

document.addEventListener('focus', function(e) {
    if (e.target && e.target.name === 'username') {
        if (!e.target.value.startsWith("+7")) {
            e.target.value = "+7";
            formatPhoneNumber(e.target); // Переформатируем номер после добавления +7
        }
    }
}, true);


document.addEventListener('blur', function(e) {
    if (e.target && e.target.name === 'username') {
        if (!e.target.value.startsWith("+7")) {
            e.target.value = "+7";
            formatPhoneNumber(e.target); // Переформатируем номер после добавления +7
        }
    }
}, true);




function formatPassport(input) {
    let value = input.value.replace(/\D/g, ''); // Удаляем все нецифровые символы

    if (value.length > 4) {
        value = value.substring(0, 4) + ' ' + value.substring(4);
    }

    if (value.length > 11) {
        value = value.substring(0, 11);
    }
    input.value = value;

    let parts = value.split(' ');
    if (parts.length > 1 && parts[1].length > 6) {
        input.value = parts[0] + ' ' + parts[1].substring(0, 6);
    }

}