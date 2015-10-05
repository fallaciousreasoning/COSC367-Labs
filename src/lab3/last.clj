(def my-last (fn [lst] (
  cond (= lst()) nil (=(rest lst)()) (first lst) :else (my-last(rest lst)))))



(println (my-last '(3 "Fred" :key 23.0)))
(println (my-last (range 7)))
(println (my-last ()))
(println (map my-last (list (range 3) (range 6) (range 7))))