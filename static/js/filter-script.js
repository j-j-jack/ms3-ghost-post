window.addEventListener('DOMContentLoaded', (event) => {
    let checkBoxes = document.getElementsByClassName('checkboxes');
    let checkBoxFilter = document.getElementsByClassName('checkbox-filter')[0];
    allCheckbox = document.getElementById('allCheckbox')
    document.getElementById('allCheckBox').addEventListener('click', function(){
        if(allCheckBox.checked == false){
            checkBoxFilter.style.background = 'rgba(183, 216, 209, 0)';
            checkBoxFilter.style.width = '0%';
            checkBoxFilter.style.height = '0%';
            checkBoxFilter.style.cursor = 'auto';
        }
        else{
            checkBoxFilter.style.background = 'rgba(0, 0, 0, .3)';
            checkBoxFilter.style.width = '100%';
            checkBoxFilter.style.height = '100%';
            checkBoxFilter.style.cursor = 'not-allowed';
        }
    })
});