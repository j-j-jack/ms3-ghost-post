window.addEventListener('DOMContentLoaded', (event) => {
    let checkBoxes = document.getElementsByClassName('checkboxes');
    let checkBoxFilter = document.getElementsByClassName('checkbox-filter')[0];
    allCheckbox = document.getElementById('allCheckbox')
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

    $('#filter-opener').click(function(){$('#filter-div').toggle('medium')});
    const fitlerMediaQuery = window.matchMedia('(min-width: 992px)')
    // https://css-tricks.com/working-with-javascript-media-queries/

    function filterOpen(e) {
  // Check if the media query is true
  if (e.matches) {
    // Then log the following message to the console
    console.log('Media Query Matched!')
    let filterDiv=document.getElementById('filter-div');
        if(filterDiv.style.display == 'none'){
            filterDiv.style.display = 'block';
        }
    }
  }
  // Register event listener
fitlerMediaQuery.addEventListener('change', filterOpen)
});