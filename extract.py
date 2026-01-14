def extract_mail_pas(cursor):

  query = """ 
    SELECT DISTINCT p.user_email
    FROM v_asignaciones_pa a
    JOIN v_pas p ON p.pa_id = a.asignpa_pa
    WHERE a.asignpa_pa_fec_alta >= CURDATE() - INTERVAL 7 DAY
      AND NOT EXISTS (
        SELECT 1
        FROM v_asignaciones_pa a2
        WHERE a2.asignpa_pa = a.asignpa_pa
          AND a2.asignpa_pa_fec_alta < a.asignpa_pa_fec_alta
      );
   """
  cursor.execute(query)

  return cursor.fetchall()