var header = document.getElementById('header');
var navigation = document.getElementById('navigation');
var content = document.getElementById('content');
var showSidebar = false;

function sidebarbotao()
{
   showSidebar =!showSidebar;
   if(showSidebar){
     navigation.style.marginLeft='-10%'; 
     navigation.style.animationName='showSidebar';
     content.style.backdropFilter = 'showDropdown';
   }
   else{
      navigation.style.marginLeft='-100%'; 
     navigation.style.animationName='';
   }

}
function closeSidebar(){
  if(showSidebar)
  {
       sidebarbotao();
  } 
}