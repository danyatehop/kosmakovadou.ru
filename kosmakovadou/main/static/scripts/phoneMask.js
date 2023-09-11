let inputClick = function(e){
    var field = e.target;
    field.placeholder = '+7 (___) ___-__-__';
}

let getInput = function(e){
    Field = e.target;
    digInput = getDigInput(Field),
    resValue = "";

    if (!digInput) Field.value = "";

    if (digInput[0] == 9) digInput = "7" + digInput;

    if(digInput.length > 1)
        resValue += "+7 (" + digInput.substring(1, 4);
    if(digInput.length > 4)
         resValue += ") " + digInput.substring(4, 7);
    if(digInput.length > 7)
        resValue += "-" + digInput.substring(7, 9);
    if(digInput.length > 9)
        resValue += "-" + digInput.substring(9, 11);

    Field.value = resValue;
}

let getDigInput = function(input){
    res = input.value.replace(/\D/g, '');
    return res
}

let backBtn = function(e){
    var field = e.target;
    if(e.code == "Backspace" && 
    field.selectionStart != field.value.length){  
            var curPos = field.selectionStart;
            setTimeout(() => {
                field.selectionStart = field.selectionEnd = curPos - 1;
            })
    }
    if(e.code == "Delete" && field.selectionStart != field.value.length){
        var curPos = field.selectionStart;
        setTimeout(() => {
            field.selectionStart = field.selectionEnd = curPos;
        })
    }
    else return;
}

var inputValue = document.getElementById('id_phone');
inputValue.addEventListener('click', inputClick);
inputValue.addEventListener('input', getInput);
inputValue.addEventListener('keydown', backBtn);
