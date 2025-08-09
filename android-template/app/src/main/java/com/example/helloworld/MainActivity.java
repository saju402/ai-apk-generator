package com.example.helloworld;

import android.os.Bundle;
import androidx.appcompat.app.AppCompatActivity;
import android.widget.LinearLayout;
import android.widget.TextView;
import android.view.Gravity;

public class MainActivity extends AppCompatActivity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        LinearLayout layout = new LinearLayout(this);
        layout.setOrientation(LinearLayout.VERTICAL);
        layout.setGravity(Gravity.CENTER);

        TextView helloText = new TextView(this);
        helloText.setText("Hello World");
        helloText.setTextSize(24);

        TextView poweredText = new TextView(this);
        poweredText.setText("Powered by Saju");
        poweredText.setTextSize(14);

        layout.addView(helloText);
        layout.addView(poweredText);

        setContentView(layout);
    }
}
