(defn member? [a ls]
  (cond
    (empty? ls) false
    (= a (first ls)) true
    :else (recur a (rest ls))))

(defn my-tr-intersection
  ([set1 set2] (my-tr-intersection set1 set2 ()))
  ([set1 set2 acc]
    (cond
      (empty? set1) acc
      (member? (first set1) set2) (recur (rest set1) set2 (cons (first set1) acc))
      :else (recur (rest set1) set2 acc)
      )))


(println (sort (my-tr-intersection (range 0 20 2) (range 0 20 3))))