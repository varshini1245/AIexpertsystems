% Facts about foods and their categories
food_category(apple, fruit).
food_category(broccoli, vegetable).
food_category(chicken, protein).
food_category(rice, carbohydrate).
% Add more food categories as needed

% Rules defining dietary recommendations for different health conditions
diet_recommendation(diabetes, Food) :-
    food_category(Food, vegetable);
    food_category(Food, protein),
    \+ food_category(Food, carbohydrate).

diet_recommendation(hypertension, Food) :-
    food_category(Food, vegetable);
    food_category(Food, fruit);
    \+ food_category(Food, sodium_rich).

diet_recommendation(obesity, Food) :-
    food_category(Food, vegetable);
    food_category(Food, fruit);
    \+ food_category(Food, high_calorie).
