package App.Infrastructure;

import org.springframework.jdbc.core.JdbcTemplate;

import java.util.List;

public abstract class BaseRepository<Item> {
    private final JdbcTemplate databaseConnection;
    public BaseRepository(JdbcTemplate databaseConnection){
        this.databaseConnection = databaseConnection;
    }

    public abstract Item get(String id) throws Exception;

    public abstract List<Item> get();

    public abstract void create(Item item);

    public abstract void delete(String id);

    public abstract void update(String id, Item item);

    public JdbcTemplate getDatabaseConnection(){
        return this.databaseConnection;
    }
}
