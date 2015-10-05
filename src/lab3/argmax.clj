(defn arg-max
  ([func lst] (arg-max func lst (first lst)))
  ([func lst best]
    (cond
      (= best nil) nil
      (= (first lst) nil) best
      (< (func best) (func (first lst))) (recur func (rest lst) (first lst))
      :else (recur func (rest lst) best)
      )
    )
  )

(println (arg-max (fn [x] (* x x)) '(1 -3 2 -5 4)))