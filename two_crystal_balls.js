const two_crystal_balls = (breaks) => {
    const jumpAmount = Math.floor(Math.sqrt(breaks));
                                                                                
    let i = jumpAmount
    for (; i < breaks; i += jumpAmount) {
        if (i >= breaks) break;
    }

    i -= jumpAmount;
        
    for (let j = 0; j <= jumpAmount && i <= breaks; ++j, ++i) {
        if (i == breaks) console.log("i", i)
    }
 
    console.log("huh")
    return null;

}

two_crystal_balls(29)