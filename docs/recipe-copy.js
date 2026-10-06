'use strict';
const copyRecipe=document.getElementById('copy-recipe');
if(copyRecipe)copyRecipe.addEventListener('click',async function(){try{await navigator.clipboard.writeText(document.getElementById('recipe-en').textContent);this.textContent='Copied';}catch{this.textContent='Select the recipe text to copy';}});
