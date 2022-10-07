package org.blackb6a.crackme;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

import java.io.UnsupportedEncodingException;

public class EnterPasswordActivity extends AppCompatActivity {
    EditText editText;
    Button button;

    String password;

    protected boolean verySecureCheck(String text){
        try {
            byte[] s = text.substring(9, text.length()-1).getBytes("US-ASCII");
            int[][] mod = {{0, 9, 2}, {2, 7, 12}, {0, 5, 10}, {1, 0, 8}, {6, 4, 9}, {4, 10, 5}, {2, 7, 12}, {4, 7, 4}, {4, 6, 12}, {6, 4, 9}, {4, 7, 4}, {0, 9, 2}, {6, 4, 9}, {2, 4, 10}, {0, 5, 10}, {2, 1, 9}, {4, 7, 4}, {6, 4, 9}, {4, 3, 11}, {4, 7, 4}, {2, 1, 9}, {0, 5, 10}, {3, 5, 11}, {1, 0, 8}, {2, 4, 10}, {2, 7, 12}, {4, 6, 12}, {2, 7, 12}, {4, 7, 4}, {4, 10, 5}, {3, 8, 0}, {4, 6, 12}, {6, 5, 0}, {4, 7, 4}, {3, 8, 0}, {5, 0, 6}, {2, 1, 9}, {4, 7, 4}, {0, 5, 10}, {4, 6, 12}, {4, 7, 4}, {0, 5, 10}, {3, 5, 11}, {4, 7, 4}, {3, 5, 11}, {4, 6, 12}, {3, 8, 0}, {2, 4, 10}, {4, 6, 12}, {4, 7, 4}, {6, 4, 9}, {4, 3, 11}, {4, 7, 4}, {4, 6, 12}, {6, 4, 9}, {2, 4, 10}, {4, 6, 12}, {5, 7, 0}, {2, 4, 10}, {2, 7, 12}};

            for (int i=0; i<=60; i++)
                if (s[i]%7 != mod[i][0] || s[i]%11 != mod[i][1] || s[i]%13 != mod[i][2])
                    return false;

            return true;

        } catch (UnsupportedEncodingException e) {
            e.printStackTrace();
            return false;
        }
    }

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_enter_password);

        editText = (EditText) findViewById(R.id.editText);
        button = (Button) findViewById(R.id.button);

        button.setOnClickListener(new View.OnClickListener(){
            @Override
            public void onClick(View v) {
                String text = editText.getText().toString();

                if((text.startsWith("hkcert22{")) &&
                        (text.endsWith("}")) &&
                        (verySecureCheck(text))){
                    Intent intent = new Intent(getApplicationContext(), MainActivity.class);
                    startActivity(intent);
                    finish();
                } else {
                    Toast.makeText(EnterPasswordActivity.this, "Wrong Password!", Toast.LENGTH_SHORT).show();
                }


            }
        });
    }
}