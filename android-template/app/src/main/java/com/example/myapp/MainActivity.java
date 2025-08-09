package com.example.myapp;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ScrollView;
import android.widget.TextView;
import androidx.appcompat.app.AppCompatActivity;
import java.util.HashMap;
import java.util.Locale;

public class MainActivity extends AppCompatActivity {
    private TextView chatArea;
    private EditText inputText;
    private Button sendButton;
    private ScrollView scrollView;
    private HashMap<String, String> botReplies;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        chatArea = findViewById(R.id.chatArea);
        inputText = findViewById(R.id.inputText);
        sendButton = findViewById(R.id.sendButton);
        scrollView = findViewById(R.id.scrollView);

        setupBotReplies();

        String appName = getString(R.string.app_name);
        chatArea.setText("Welcome to " + appName + "!\n\n");

        sendButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                String user = inputText.getText().toString().trim();
                if (user.isEmpty()) return;

                appendToChat("You: " + user + "\n");
                String key = user.toLowerCase(Locale.ROOT);
                String reply = botReplies.getOrDefault(key, "Sorry, I don't understand.");
                appendToChat("Bot: " + reply + "\n\n");
                inputText.setText("");
                scrollView.post(() -> scrollView.fullScroll(View.FOCUS_DOWN));
            }
        });
    }

    private void setupBotReplies() {
        botReplies = new HashMap<>();
        botReplies.put("hi", "Hello! How can I help you?");
        botReplies.put("hello", "Hello! How can I help you?");
        botReplies.put("how are you", "I am fine! Ready to chat with you.");
        botReplies.put("bye", "Goodbye! Have a great day.");
        botReplies.put("what is your name", "I'm your friendly AI chatbot.");
    }

    private void appendToChat(String message) {
        chatArea.append(message);
    }
}
