# import itertools
# import numpy as np
#
# # Define card ranks and suits
# ranks = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
# suits = ['♠', '♥', '♣', '♦']
#
# # Generate all combinations of two cards
# all_two_card_hands = list(itertools.combinations([f"{r}{s}" for r in ranks for s in suits], 2))
#
# # Group hands into suited, off-suited, and pairs
# hands_dict = {
#     "pair": [],
#     "suited": [],
#     "off-suited": []
# }
#
# for hand in all_two_card_hands:
#     rank1, suit1 = hand[0][:-1], hand[0][-1]
#     rank2, suit2 = hand[1][:-1], hand[1][-1]
#
#     if rank1 == rank2:
#         hands_dict['pair'].append(hand)
#     elif suit1 == suit2:
#         hands_dict['suited'].append(hand)
#     else:
#         hands_dict['off-suited'].append(hand)
#
# # Simulated "winning strength" for each hand category (based on general poker principles)
# # We'll assign rough probabilities based on common hand rankings (pairs > suited > off-suited)
# # For simplicity, these are placeholders and can be refined with simulations
#
# # Approximate win probabilities
# np.random.seed(42)
# pair_probabilities = np.random.uniform(0.65, 0.9, len(hands_dict['pair']))
# suited_probabilities = np.random.uniform(0.5, 0.75, len(hands_dict['suited']))
# off_suited_probabilities = np.random.uniform(0.3, 0.55, len(hands_dict['off-suited']))
#
# # Combine all probabilities into a single list
# all_hands_with_probabilities = {
#     "hand": hands_dict['pair'] + hands_dict['suited'] + hands_dict['off-suited'],
#     "probability": np.concatenate([pair_probabilities, suited_probabilities, off_suited_probabilities])
# }
#
# # Sort hands by probability for ranking
# sorted_hands_with_probabilities = sorted(
#     zip(all_hands_with_probabilities['hand'], all_hands_with_probabilities['probability']), key=lambda x: x[1],
#     reverse=True)
#
# # Display top and bottom few entries for overview
# sorted_hands_with_probabilities[:5], sorted_hands_with_probabilities[-5:]
