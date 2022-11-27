#!/bin/bash

users=("nipponkairagi" "nipponichi8" "nippon_ukuraina" "jda1BekUDve1ccx" "CYXuAxfGlfFzZCT" "Aahi69Mai" "toshio_tamogami" "hyakutanaoki" "ifvoc_rashinban" "ucjptw")
#海乱鬼　一色　ナザレンコ　加藤清隆　闇のくまさん　水原 田母神 百田尚樹 ラシンバン 統一教会
for user in ${users[@]}; do
  echo $user
  python get_tweets.py $user
done