USE mfb56;
DELIMITER $$
CREATE PROCEDURE InsertPaymentThenRegister(
    IN amount Double,
    IN payment_method VARCHAR(20),
    IN song_id INT
)
BEGIN
    DECLARE paymentId INT; -- Variable to hold the ID of the inserted payment
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        ROLLBACK;
        SELECT 'Transaction failed, rolled back' AS message;
    END;

    -- Start the transaction
    START TRANSACTION;

    -- Insert into the payments table and get the inserted ID
    INSERT INTO payments (amount, payment_method, song_id, payment_date)
    VALUES (amount, payment_method, song_id,now());

    -- Get the ID of the newly inserted payment
    SET paymentId = LAST_INSERT_ID();

    -- Ensure the payment ID was created before proceeding
    IF paymentId IS NULL THEN
        ROLLBACK;
        SELECT 'Failed to insert into payments, rolling back' AS message;
    END IF;

    -- Insert into the registration table using the payment ID
    INSERT INTO copyright (fk_song_id,copyright_holder)
    VALUES (song_id,'song_registed');

    -- Commit the transaction if both inserts are successful
    COMMIT;

    SELECT 'Transaction successful, data committed' AS message;
END$$
DELIMITER ;
