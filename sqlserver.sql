-- create a user
USE master;
GO
CREATE LOGIN vc_user WITH PASSWORD = '...';
GO

USE YourDatabaseName;
GO
CREATE USER ReadOnlyUser FOR LOGIN ReadOnlyUser;
EXEC sp_addrolemember 'db_datareader', 'ReadOnlyUser';

-------------------------------------------------------------------

-- see linked servers
EXEC sp_linkedservers;

-------------------------------------------------------------------

-- see current user
SELECT
    SYSTEM_USER AS 'System/Login Name',
    CURRENT_USER AS 'Current DB User',
    SESSION_USER AS 'Session User',
    
	-- Returns the original login  that connected to SQL Server, even if the session has switched contexts using EXECUTE AS. 
	ORIGINAL_LOGIN() AS 'Original Login';

-------------------------------------------------------------------

-- give a linkedserver to a login
-- give access to a linkedsever for a user
-- This is useful when the user connects via SQL authentication and you want to map them to a specific user on the remote server. 

EXEC sp_addlinkedsrvlogin
    @rmtsrvname = 'DJANGO',
    @useself = 'false',
    @locallogin = 'vc_user', -- e.g., 'ReadOnlyUser'
    @rmtuser = 'salesnetwork_r',        -- e.g., 'RemoteDBUser'
    @rmtpassword = '...'; -- password for RemoteUserLogin