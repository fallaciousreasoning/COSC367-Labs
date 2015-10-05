(defn step [func, add]
  (fn [arg] (add (func arg))))

(defn compose [& args]
  (if
    (empty? args) identity
    (reduce step args)
    )
  )

(def $3x+10 (compose (partial * 3) (partial + 10)))
(println (map $3x+10 (range 5)))
;
(def my-odd? (compose even? not))
(println (filter my-odd? (range 10)))

(println (map (compose) (range 10)))

(println (map (compose (partial * 2) (partial + 3) (partial * 4)) (range 10)))