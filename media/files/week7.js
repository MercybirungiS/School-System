///modules ave exposed bits
//they have depemdancies
//help keep organized code bases 
//help share and re use code
var myDIYmodule=(function(){
    //PRIVATE variables
    var counter=0;
    //exposed functions
    return{
        increment:function(){
            counter+=1;

        },
    print:function(){
        console.log(counter);
    }
    }

}());