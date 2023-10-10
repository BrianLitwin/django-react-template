(ns client.events
  (:require
   [re-frame.core :as re-frame]
   [client.db :as db]
   [ajax.core :as ajax]))

(re-frame/reg-event-db
 ::initialize-db
 (fn [_ _]
   db/default-db))

(defn fetch-flashcards []
  (ajax/GET "http://localhost:8010/cards/"
            {:response-format (ajax/json-response-format {:keywords? true})
             :handler (fn [response]
                        (prn response)
                        )}))