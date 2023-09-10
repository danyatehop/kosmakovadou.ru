let placeholder = function(e){
    e.target.placeholder = '+7(___)-___-__-__';
}

let getInput = function(e){
    Field = e.target;
    digInput = getDigInput(Field),
    resValue = "";

    if (!digInput) Field.value = "";

    if (digInput[0] == 9) digInput = "7" + digInput;

    console.log(digInput.length)

    if(digInput.length > 1)
        resValue += "+7(" + digInput.substring(1, 4);
    if(digInput.length > 4)
         resValue += ")-" + digInput.substring(4, 7);
    if(digInput.length > 7)
        resValue += "-" + digInput.substring(7, 9);
    if(digInput.length > 9)
        resValue += "-" + digInput.substring(9, 11);

    console.log(digInput);
    Field.value = resValue;
}

let getDigInput = function(input){
    res = input.value.replace(/\D/g, '');
    return res
}

var inputValue = document.getElementById('id_phone');
inputValue.addEventListener('click', placeholder);
inputValue.addEventListener('input', getInput);