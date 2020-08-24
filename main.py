function resetGame () {
    prevRoll = 0
    playing = 1
}
function createDieImages () {
    dieImages = []
    dieImages.push(images.createImage(`
        . . . . .
        . . . . .
        . . # . .
        . . . . .
        . . . . .
        `))
    dieImages.push(images.createImage(`
        . . . . .
        . # . . .
        . . . . .
        . . . # .
        . . . . .
        `))
    dieImages.push(images.createImage(`
        . . . . .
        . . . # .
        . . # . .
        . # . . .
        . . . . .
        `))
    dieImages.push(images.createImage(`
        . . . . .
        . # . # .
        . . . . .
        . # . # .
        . . . . .
        `))
    dieImages.push(images.createImage(`
        . . . . .
        . # . # .
        . . # . .
        . # . # .
        . . . . .
        `))
    dieImages.push(images.createImage(`
        . . . . .
        . # . # .
        . # . # .
        . # . # .
        . . . . .
        `))
}
function stepGame () {
    roll = randint(1, 6)
    showRoll(roll, 1)
    if (prevRoll + roll == 7) {
        playing = 0
        showWin(prevRoll, roll)
    }
    prevRoll = roll
}
function showRoll (roll: number, direction: number) {
    dieImages[roll - 1].scrollImage(direction, 200)
}
function showWin (die1: number, die2: number) {
    basic.showIcon(IconNames.Fabulous)
    while (playing == 0) {
        showRoll(die1, 1)
        showRoll(die2, 1)
    }
}
function initOnce () {
    createDieImages()
}
input.onGesture(Gesture.ScreenDown, function () {
    resetGame()
    resetWait()
})
input.onGesture(Gesture.Shake, function () {
    if (playing == 1) {
        stepGame()
    }
})
function resetWait () {
    while (!(input.isGesture(Gesture.ScreenUp))) {
        basic.showIcon(IconNames.SmallDiamond)
        basic.showIcon(IconNames.Diamond)
    }
    basic.clearScreen()
}
let roll = 0
let dieImages: Image[] = []
let playing = 0
let prevRoll = 0
initOnce()
resetGame()
basic.showString("Dice 7")
