const openPopUp = document.getElementById('open_pop_up');
const closePopUp = document.getElementById('pop_up_close');
const popUp = document.getElementById('pop_up');

openPopUp.addEventListener('click', function(e){
  e.preventDefault();
  popUp.classList.add('active');

})
closePopUp.addEventListener('click',()=>{
  popUp.classList.remove('active');
})
var el_1 = document.getElementsByTagName('div1');
var el_2 = document.getElementsByTagName('div1');

function changeCollectionы(elements){
  for(var i = 0; i<elements.length;i++){
    elements[i].innerHTML = 'ру';
  }
}

function changeCollection(elements){
  for(var i = 0; i<elements.length;i++){
    elements[i].innerHTML = 'Создать сайт про бизнеса';
  }
}













