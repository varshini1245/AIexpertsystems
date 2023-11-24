% Facts about fruits and their colors
fruit_color(apple, red).
fruit_color(banana, yellow).
fruit_color(grape, purple).
fruit_color(orange, orange).
fruit_color(strawberry, red).
fruit_color(watermelon, green).
fruit_color(blueberry, blue).
fruit_color(mango, yellow).
% Add more fruits and their colors as needed

% Rule to find fruits based on a specific color
fruit_with_color(Color, Fruit) :-
    fruit_color(Fruit, Color).
